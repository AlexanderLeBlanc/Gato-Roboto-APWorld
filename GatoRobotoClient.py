from __future__ import annotations
import os
import sys
import asyncio
import typing
import bsdiff4
import shutil
import json

import Utils

from NetUtils import NetworkItem, ClientStatus
from worlds import gatoroboto
from MultiServer import mark_raw
from CommonClient import CommonContext, server_loop, \
    gui_enabled, ClientCommandProcessor, logger, get_base_parser
from Utils import async_start

"""
Notes on things ive learned:
locations_checked = list maintained by client of locations youve checked
checked_locations = list from server of locations youve checked
"""

class GatoRobotoCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx):
        super().__init__(ctx) 
        
    def print_log(msg):
        logger.info(msg)
        
    @mark_raw
    def _cmd_auto_patch(self, steaminstall: typing.Optional[str] = None):
        """Patch the game automatically."""
        if isinstance(self.ctx, GatoRobotoContext):
            
            #os.makedirs(name=Utils.user_path("Gato Roboto/anim"), exist_ok=True)
            tempInstall = steaminstall
            if not os.path.isfile(os.path.join(tempInstall, "data.win")):
                tempInstall = None
            if tempInstall is None:
                tempInstall = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Gato Roboto"
                if not os.path.exists(tempInstall):
                    tempInstall = "C:\\Program Files\\Steam\\steamapps\\common\\Gato Roboto"
            elif not os.path.exists(tempInstall):
                tempInstall = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Gato Roboto"
                if not os.path.exists(tempInstall):
                    tempInstall = "C:\\Program Files\\Steam\\steamapps\\common\\Gato Roboto"
            if not os.path.exists(tempInstall) or not os.path.exists(tempInstall) or not os.path.isfile(os.path.join(tempInstall, "data.win")):
                self.output("ERROR: Cannot find Gato Roboto. Please rerun the command with the correct folder."
                            " command. \"/auto_patch (Steam directory)\".")
            else:                
                self.ctx.patch_game(tempInstall)
                self.output("Patching successful!")

class GatoRobotoContext(CommonContext):
    tags = {"AP", "Online"}
    game = "Gato Roboto"
    command_processor = GatoRobotoCommandProcessor
    save_game_folder = os.path.expandvars(r"%localappdata%/GatoRoboto")
    checks_to_consume = []
    cur_client_items = []
    read_client_items = False
    cur_start_index = 0
    
    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        self.game = "Gato Roboto"
        self.syncing = False
        
        # Magical item handling value that I don't understand
        self.items_handling = 0b111
        
        # self.save_game_folder: Files go in this path to pass data between us and the actual game
        self.save_game_folder = os.path.expandvars(r"%localappdata%/GatoRoboto")
        
    def patch_game(self, filepath):
        os.makedirs(name=filepath + "/VanillaData", exist_ok=True)
        shutil.copy(filepath + "/data.win", filepath + "/VanillaData")
        with open(filepath + "/data.win", "rb") as f:
            patchedFile = bsdiff4.patch(f.read(), gatoroboto.data_path("patch.bsdiff"))
        with open(filepath + "/data.win", "wb") as f:
            f.write(patchedFile)

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)

        await self.get_username()
        await self.send_connect()

    def on_package(self, cmd, args):        
        if (cmd == 'Connected'):
            self.game = self.slot_info[self.slot].game
        
        async_start(process_gatoroboto_cmd(self, cmd, args))
        
    async def connect(self, address: typing.Optional[str] = None):
        await super().connect(address)

    async def disconnect(self, allow_autoreconnect: bool = False):
        await super().disconnect(allow_autoreconnect)

    async def connection_closed(self):
        await super().connection_closed()

    async def shutdown(self):
        await super().shutdown()
        
    def run_gui(self):
        from kvui import GameManager

        class UTManager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago Gato Roboto Client"

        self.ui = UTManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")
        
async def game_watcher(ctx: GatoRobotoContext):    
    printed_connecting = False
     
    while not ctx.exit_event.is_set():
        await asyncio.sleep(0.1)
        
        if not printed_connecting:
            ctx.command_processor.print_log("Waiting for Connection to Game")
            printed_connecting = True
        
        #watch for received locations from game
        if os.path.exists(ctx.save_game_folder + "/locations.json"):   
            with open(ctx.save_game_folder + "/locations.json", 'r+') as f:
                locations_in = get_clean_game_comms_file(f)
                
                sending = []
                
                #print("Missing Locations")
                #print(ctx.missing_locations)
                
                for key in locations_in:
                    if str(key).isdigit():
                        print("Location check: " + str(key) + " // " + str(ctx.missing_locations.__contains__(int(key))) + " // " + str(int(locations_in[str(key)]) > 0))
                        if ctx.missing_locations.__contains__(int(key)) and int(locations_in[str(key)]) > 0:
                            sending.append(int(key))
                
                if len(sending) != 0:
                    await ctx.send_msgs([{"cmd": "LocationChecks", "locations": sending}])
            
            os.remove(ctx.save_game_folder + "/locations.json")
        
        #check if wincon present
        if os.path.exists(ctx.save_game_folder + "/victory.json"):
            if not ctx.finished_game:
                await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                
        #check if game disconnects
        if os.path.exists(ctx.save_game_folder + "/off.json"):
            ctx.command_processor.print_log("Lost Connection to Game")
            ctx.command_processor.print_log("Waiting for Connection to Game")
            os.remove(ctx.save_game_folder + "/off.json")
            ctx.cur_client_items = []
            ctx.read_client_items = False
              
        #read initial data for syncing items with the client
        if not ctx.read_client_items and os.path.exists(ctx.save_game_folder + "/init.json"):
            ctx.command_processor.print_log("Connected to Game")
            
            ctx.read_client_items = True
            
            with open(ctx.save_game_folder + "/init.json", 'r+') as f:
                items_init = get_clean_game_comms_file(f)
                
                for key in items_init:
                    ctx.cur_client_items.append(int(key))
                    
            os.remove(ctx.save_game_folder + "/init.json")
        
        #consume items in fifo order, filter out received items
        if len(ctx.checks_to_consume) > 0 and ctx.read_client_items and not os.path.exists(ctx.save_game_folder + "/items.json"):
            flag = True
            while(len(ctx.checks_to_consume) > 0 and flag):
                cur_item = ctx.checks_to_consume.pop(0)
                
                if not ctx.cur_client_items.__contains__(int(cur_item.item)):
                    ctx.cur_client_items.append(int(cur_item.item))
                    
                    item_in = {
                        "item": int(cur_item.item),
                        "item_index": len(ctx.cur_client_items)
                    }
                    
                    item_in_json = json.dumps(item_in, indent=4)
            
                    with open(ctx.save_game_folder + "/tmp_it.json", 'w') as f:
                        f.write(item_in_json)
                
                    os.rename(ctx.save_game_folder + "/tmp_it.json", ctx.save_game_folder + "/items.json")

                    flag = True                        

# Looks like most of these automatically call in the process_server_cmd() method in CommonClient.py
# Not sure if we are overriding it or just executing our own code alongside it
async def process_gatoroboto_cmd(ctx: GatoRobotoContext, cmd: str, args: dict):
    if cmd == "Connected":
        print("CONNECTED SHII")
        
        # Do all file init here
        if not os.path.exists(ctx.save_game_folder):
            os.mkdir(ctx.save_game_folder)
            
    elif cmd == "RoomInfo":
        # Probably not necessary from looking at other clients
        print("Info: " + str(ctx.seed_name) + " : " + str(args["seed_name"]))
    elif cmd == "LocationInfo":
        # Potentially for hinting?
        print("Loc. Info: " + str(args["locations"]))
    elif cmd == "RoomUpdate":
        # Update checked locations in files for game
        print("Room Updates")
    elif cmd == "ReceivedItems":
        # Big logical state machine to track item index into what item gets written to file
        print("GOT SOME ITEMS")
        print(str(args["items"]))
        ctx.watcher_event.set()
        
        start_index = args["index"]
        
        if start_index == 0:
            ctx.items_received = []
        elif start_index != len(ctx.items_received):
            sync_msg = [{"cmd": "Sync"}]
            if ctx.locations_checked:
                sync_msg.append({"cmd": "LocationChecks",
                                 "locations": list(ctx.locations_checked)})
            await ctx.send_msgs(sync_msg)
        
        if start_index == len(ctx.items_received):
            
            #Send items to items queue
            for item in args["items"]:
                net_item = NetworkItem(*item)
                ctx.checks_to_consume.append(net_item)
            
            ctx.cur_start_index = start_index

def get_clean_game_comms_file(f):
    """
    Reads a JSON file, removes any trailing or embedded null characters (\x00),
    and ensures the file is valid JSON before saving the cleaned version.
    """
    content = f.read()

    cleaned_content = content.replace("\x00", "").strip()

    if not cleaned_content.endswith("}"):
        cleaned_content += "}"

    try:
        cleaned_json = json.loads(cleaned_content)
    except json.JSONDecodeError:
        print("Error: Invalid JSON file, unable to fix.")
        return
    
    if content != cleaned_content:
        f.seek(0)
        f.truncate()
        f.write(cleaned_content)
        print("JSON file cleaned successfully.")
        
    return cleaned_json
                    
def main():        
    Utils.init_logging("GatoRobotoClient", exception_logger="Client")

    async def _main():
        ctx = GatoRobotoContext(None, None)
        
        if os.path.exists(ctx.save_game_folder + "/item.json"):
            os.remove(ctx.save_game_folder + "/item.json")
            
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
        asyncio.create_task(
            game_watcher(ctx), name="GatoRobotoProgressionWatcher")

        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        await ctx.exit_event.wait()
        await ctx.shutdown()

    import colorama

    colorama.init()

    asyncio.run(_main())
    colorama.deinit()

parser = get_base_parser(description="Gato Roboto Client, for text interfacing.")
args = parser.parse_args()
main()
        


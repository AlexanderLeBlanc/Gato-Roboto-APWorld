import math

from BaseClasses import ItemClassification
from worlds.generic.Rules import add_rule, item_name_in_locations, set_rule
from . import Options
from . import GatoRobotoWorld
from .Names import RegionName
from .Names import ItemName
from .Names import LocationName

from .Locations import GatoRobotoLocation

def set_rules(world: GatoRobotoWorld):    
    #Set Checks for Landing Site
    set_rule(world.get_location(LocationName.healthkit_2),
             lambda state: state.has(ItemName.module_missile, world.player))
    set_rule(world.get_location(LocationName.cartridge_1),
             lambda state: state.has(ItemName.module_missile, world.player))
    set_rule(world.get_location(LocationName.cartridge_2),
             lambda state: state.has(ItemName.module_missile, world.player))
    set_rule(world.get_location(LocationName.module_2),
             lambda state: state.has(ItemName.module_spinjump, world.player) and sum(state.has(item, world.player) for item in [
                ItemName.progressive_vent_1, ItemName.progressive_vent_2, ItemName.progressive_vent_3
             ]) >= 3)
    
    
    #Set Checks for Nexus
    set_rule(world.get_region(RegionName.region_2).entrances[0],
            lambda state: state.has(ItemName.module_missile, world.player))
    set_rule(world.get_location(LocationName.healthkit_3), 
             lambda state: state.has(ItemName.module_spinjump, world.player) or (world.options.rocket_jumps and state.has(ItemName.module_coolant, world.player)))
    set_rule(world.get_location(LocationName.healthkit_4), 
             lambda state: state.has(ItemName.module_spinjump, world.player) or (world.options.rocket_jumps))
    set_rule(world.get_location(LocationName.cartridge_3), 
             lambda state: sum(state.has(item, world.player) for item in [
                ItemName.progressive_aqueduct_1, ItemName.progressive_aqueduct_2, ItemName.progressive_aqueduct_3
             ]) >= 3 or (world.options.rocket_jumps and state.has(ItemName.module_coolant, world.player)))
    set_rule(world.get_location(LocationName.cartridge_4), 
            lambda state: state.has(ItemName.module_spinjump, world.player) or world.options.logic_difficulty == 1)
    set_rule(world.get_location(LocationName.cartridge_5), 
             lambda state: sum(state.has(item, world.player) for item in [
                ItemName.progressive_vent_1, ItemName.progressive_vent_2, ItemName.progressive_vent_3
             ]) >= 3 or world.options.logic_difficulty == 1)
    set_rule(world.get_location(LocationName.module_3), 
             lambda state: sum(state.has(item, world.player) for item in [
                ItemName.cartridge_1, ItemName.cartridge_2, ItemName.cartridge_3,
                ItemName.cartridge_4, ItemName.cartridge_5, ItemName.cartridge_6,
                ItemName.cartridge_7, ItemName.cartridge_8, ItemName.cartridge_9,
                ItemName.cartridge_10, ItemName.cartridge_11, ItemName.cartridge_12,
                ItemName.cartridge_13, ItemName.cartridge_14
             ]) >= 7)
    set_rule(world.get_location(LocationName.module_4), 
             lambda state: sum(state.has(item, world.player) for item in [
                ItemName.cartridge_1, ItemName.cartridge_2, ItemName.cartridge_3,
                ItemName.cartridge_4, ItemName.cartridge_5, ItemName.cartridge_6,
                ItemName.cartridge_7, ItemName.cartridge_8, ItemName.cartridge_9,
                ItemName.cartridge_10, ItemName.cartridge_11, ItemName.cartridge_12,
                ItemName.cartridge_13, ItemName.cartridge_14
             ]) >= 14)
    
    #Set Checks for Aquaducts
    set_rule(world.get_location(LocationName.healthkit_5), 
            lambda state: sum(state.has(item, world.player) for item in [
                ItemName.progressive_aqueduct_1, ItemName.progressive_aqueduct_2, ItemName.progressive_aqueduct_3
             ]) >= 1)
    set_rule(world.get_location(LocationName.healthkit_6), 
             lambda state: sum(state.has(item, world.player) for item in [
                ItemName.progressive_aqueduct_1, ItemName.progressive_aqueduct_2, ItemName.progressive_aqueduct_3
             ]) >= 3)
    set_rule(world.get_location(LocationName.cartridge_6), 
            lambda state: state.has(ItemName.module_spinjump, world.player) and sum(state.has(item, world.player) for item in [
                ItemName.progressive_aqueduct_1, ItemName.progressive_aqueduct_2, ItemName.progressive_aqueduct_3
             ]) >= 3)
    set_rule(world.get_location(LocationName.cartridge_7), 
             lambda state: state.has(ItemName.module_spinjump, world.player) and sum(state.has(item, world.player) for item in [
                ItemName.progressive_aqueduct_1, ItemName.progressive_aqueduct_2, ItemName.progressive_aqueduct_3
             ]) >= 3)
    set_rule(world.get_location(LocationName.cartridge_8), 
             lambda state: sum(state.has(item, world.player) for item in [
                ItemName.progressive_aqueduct_1, ItemName.progressive_aqueduct_2, ItemName.progressive_aqueduct_3
             ]) >= 2)
    set_rule(world.get_location(LocationName.module_5), 
             lambda state: sum(state.has(item, world.player) for item in [
                ItemName.progressive_aqueduct_1, ItemName.progressive_aqueduct_2, ItemName.progressive_aqueduct_3
             ]) >= 3)
    set_rule(world.get_location(LocationName.aqueduct_2), 
             lambda state: sum(state.has(item, world.player) for item in [
                ItemName.progressive_aqueduct_1, ItemName.progressive_aqueduct_2, ItemName.progressive_aqueduct_3
             ]) >= 1)
    set_rule(world.get_location(LocationName.aqueduct_3), 
             lambda state: sum(state.has(item, world.player) for item in [
                ItemName.progressive_aqueduct_1, ItemName.progressive_aqueduct_2, ItemName.progressive_aqueduct_3
             ]) >= 2)
    
    #Heater Logic
    set_rule(world.get_region(RegionName.region_4).entrances[0],
             lambda state: state.has(ItemName.module_spinjump, world.player) or world.options.rocket_jumps)
    set_rule(world.get_location(LocationName.healthkit_7), 
             lambda state: sum(state.has(item, world.player) for item in [
                ItemName.progressive_heater_1, ItemName.progressive_heater_2, ItemName.progressive_heater_3
             ]) >= 3 or world.options.rocket_jumps)
    set_rule(world.get_location(LocationName.healthkit_8), 
             lambda state: sum(state.has(item, world.player) for item in [
                ItemName.progressive_heater_1, ItemName.progressive_heater_2, ItemName.progressive_heater_3
             ]) >= 3 or world.options.rocket_jumps)
    set_rule(world.get_location(LocationName.cartridge_9), 
             lambda state: sum(state.has(item, world.player) for item in [
                ItemName.progressive_heater_1, ItemName.progressive_heater_2, ItemName.progressive_heater_3
             ]) >= 3 or world.options.rocket_jumps)
    set_rule(world.get_location(LocationName.cartridge_10), 
             lambda state: sum(state.has(item, world.player) for item in [
                ItemName.progressive_heater_1, ItemName.progressive_heater_2, ItemName.progressive_heater_3
             ]) >= 3 or world.options.rocket_jumps)
    set_rule(world.get_location(LocationName.cartridge_11), 
             lambda state: sum(state.has(item, world.player) for item in [
                ItemName.progressive_heater_1, ItemName.progressive_heater_2, ItemName.progressive_heater_3
             ]) >= 3 or world.options.rocket_jumps)
    set_rule(world.get_location(LocationName.module_6), 
             lambda state: sum(state.has(item, world.player) for item in [
                ItemName.progressive_heater_1, ItemName.progressive_heater_2, ItemName.progressive_heater_3
             ]) >= 3 or world.options.rocket_jumps)
    set_rule(world.get_location(LocationName.module_7), 
             lambda state: sum(state.has(item, world.player) for item in [
                ItemName.progressive_heater_1, ItemName.progressive_heater_2, ItemName.progressive_heater_3
             ]) >= 2 or world.options.rocket_jumps)
    set_rule(world.get_location(LocationName.heater_3), 
             lambda state: sum(state.has(item, world.player) for item in [
                ItemName.progressive_heater_1, ItemName.progressive_heater_2, ItemName.progressive_heater_3
             ]) >= 2)
    set_rule(world.get_location(LocationName.heater_2), 
             lambda state: sum(state.has(item, world.player) for item in [
                ItemName.progressive_heater_1, ItemName.progressive_heater_2, ItemName.progressive_heater_3
             ]) >= 1)
    
    #Ventilation logic
    set_rule(world.get_region(RegionName.region_5).entrances[0],
        lambda state: sum(state.has(item, world.player) for item in [
                ItemName.progressive_aqueduct_1, ItemName.progressive_aqueduct_2, ItemName.progressive_aqueduct_3
             ]) >= 3 and sum(state.has(item, world.player) for item in [
                ItemName.progressive_heater_1, ItemName.progressive_heater_2, ItemName.progressive_heater_3
             ]) >= 3)
    set_rule(world.get_location(LocationName.healthkit_9), 
             lambda state: sum(state.has(item, world.player) for item in [
                ItemName.progressive_vent_1, ItemName.progressive_vent_2, ItemName.progressive_vent_3
             ]) >= 1)
    set_rule(world.get_location(LocationName.cartridge_12), 
             lambda state: sum(state.has(item, world.player) for item in [
                ItemName.progressive_vent_1, ItemName.progressive_vent_2, ItemName.progressive_vent_3
             ]) >= 3)
    set_rule(world.get_location(LocationName.cartridge_13), 
             lambda state: sum(state.has(item, world.player) for item in [
                ItemName.progressive_vent_1, ItemName.progressive_vent_2, ItemName.progressive_vent_3
             ]) >= 3)
    set_rule(world.get_location(LocationName.module_8), 
             lambda state: sum(state.has(item, world.player) for item in [
                ItemName.progressive_vent_1, ItemName.progressive_vent_2, ItemName.progressive_vent_3
             ]) >= 1)
    set_rule(world.get_location(LocationName.vent_2), 
             lambda state: sum(state.has(item, world.player) for item in [
                ItemName.progressive_vent_1, ItemName.progressive_vent_2, ItemName.progressive_vent_3
             ]) >= 1)
    set_rule(world.get_location(LocationName.vent_3), 
             lambda state: sum(state.has(item, world.player) for item in [
                ItemName.progressive_vent_1, ItemName.progressive_vent_2, ItemName.progressive_vent_3
             ]) >= 1)
    
    #Incubator logic
    set_rule(world.get_region(RegionName.region_6).entrances[0],
        lambda state: state.has(ItemName.module_decoder, world.player) and sum(state.has(item, world.player) for item in [
                ItemName.progressive_vent_1, ItemName.progressive_vent_2, ItemName.progressive_vent_3
             ]) >= 3 and sum(state.has(item, world.player) for item in [
                ItemName.progressive_heater_1, ItemName.progressive_heater_2, ItemName.progressive_heater_3
             ]) >= 3)
    set_rule(world.get_location(LocationName.healthkit_10), 
            lambda state: state.has(ItemName.module_spinjump, world.player) and state.has(ItemName.module_hopper, world.player) and state.has(ItemName.module_phase, world.player))
    
    
    
    
    
    
    
    
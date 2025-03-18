from typing import Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification
from .Names import ItemName

gato_roboto_base_id: int = 10000

class GatoRobotoItem(Item):
    game = "Gato Roboto"
    
class GatoRobotoItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    
modules_item_data_table: Dict[str, GatoRobotoItemData] = {
    ItemName.module_bigshot: GatoRobotoItemData(gato_roboto_base_id + 212, ItemClassification.progression),
    ItemName.module_coolant: GatoRobotoItemData(gato_roboto_base_id + 211, ItemClassification.progression),
    ItemName.module_decoder: GatoRobotoItemData(gato_roboto_base_id + 209, ItemClassification.progression),
    ItemName.module_hopper: GatoRobotoItemData(gato_roboto_base_id + 214, ItemClassification.progression),
    ItemName.module_missile: GatoRobotoItemData(gato_roboto_base_id + 210, ItemClassification.progression),
    ItemName.module_phase: GatoRobotoItemData(gato_roboto_base_id + 216, ItemClassification.progression),
    ItemName.module_repeater: GatoRobotoItemData(gato_roboto_base_id + 213, ItemClassification.useful),
    ItemName.module_spinjump: GatoRobotoItemData(gato_roboto_base_id + 215, ItemClassification.progression)
}

healthkits_item_data_table: Dict[str, GatoRobotoItemData] = {
    ItemName.healthkit_1: GatoRobotoItemData(gato_roboto_base_id + 16, ItemClassification.progression),
    ItemName.healthkit_2: GatoRobotoItemData(gato_roboto_base_id + 17, ItemClassification.progression),
    ItemName.healthkit_3: GatoRobotoItemData(gato_roboto_base_id + 18, ItemClassification.progression),
    ItemName.healthkit_4: GatoRobotoItemData(gato_roboto_base_id + 19, ItemClassification.progression),
    ItemName.healthkit_5: GatoRobotoItemData(gato_roboto_base_id + 20, ItemClassification.progression),
    ItemName.healthkit_6: GatoRobotoItemData(gato_roboto_base_id + 21, ItemClassification.progression),
    ItemName.healthkit_7: GatoRobotoItemData(gato_roboto_base_id + 22, ItemClassification.progression),
    ItemName.healthkit_8: GatoRobotoItemData(gato_roboto_base_id + 23, ItemClassification.progression),
    ItemName.healthkit_9: GatoRobotoItemData(gato_roboto_base_id + 24, ItemClassification.progression),
    ItemName.healthkit_10: GatoRobotoItemData(gato_roboto_base_id + 25, ItemClassification.progression)
}

cartidges_item_data_table: Dict[str, GatoRobotoItemData] = {
    ItemName.cartridge_1: GatoRobotoItemData(gato_roboto_base_id + 2, ItemClassification.progression),
    ItemName.cartridge_2: GatoRobotoItemData(gato_roboto_base_id + 3, ItemClassification.progression),
    ItemName.cartridge_3: GatoRobotoItemData(gato_roboto_base_id + 4, ItemClassification.progression),
    ItemName.cartridge_4: GatoRobotoItemData(gato_roboto_base_id + 5, ItemClassification.progression),
    ItemName.cartridge_5: GatoRobotoItemData(gato_roboto_base_id + 6, ItemClassification.progression),
    ItemName.cartridge_6: GatoRobotoItemData(gato_roboto_base_id + 7, ItemClassification.progression),
    ItemName.cartridge_7: GatoRobotoItemData(gato_roboto_base_id + 8, ItemClassification.progression),
    ItemName.cartridge_8: GatoRobotoItemData(gato_roboto_base_id + 9, ItemClassification.progression),
    ItemName.cartridge_9: GatoRobotoItemData(gato_roboto_base_id + 10, ItemClassification.progression),
    ItemName.cartridge_10: GatoRobotoItemData(gato_roboto_base_id + 11, ItemClassification.progression),
    ItemName.cartridge_11: GatoRobotoItemData(gato_roboto_base_id + 12, ItemClassification.progression),
    ItemName.cartridge_12: GatoRobotoItemData(gato_roboto_base_id + 13, ItemClassification.progression),
    ItemName.cartridge_13: GatoRobotoItemData(gato_roboto_base_id + 14, ItemClassification.progression),
    ItemName.cartridge_14: GatoRobotoItemData(gato_roboto_base_id + 15, ItemClassification.progression)
}

heater_events_item_data_table: Dict[str, GatoRobotoItemData] = {
    ItemName.progressive_heater_1: GatoRobotoItemData(gato_roboto_base_id + 254, ItemClassification.progression),
    ItemName.progressive_heater_2: GatoRobotoItemData(gato_roboto_base_id + 255, ItemClassification.progression),
    ItemName.progressive_heater_3: GatoRobotoItemData(gato_roboto_base_id + 256, ItemClassification.progression),
}

aqueduct_events_item_data_table: Dict[str, GatoRobotoItemData] = {
    ItemName.progressive_aqueduct_1: GatoRobotoItemData(gato_roboto_base_id + 237, ItemClassification.progression),
    ItemName.progressive_aqueduct_2: GatoRobotoItemData(gato_roboto_base_id + 238, ItemClassification.progression),
    ItemName.progressive_aqueduct_3: GatoRobotoItemData(gato_roboto_base_id + 239, ItemClassification.progression),
}

vent_events_item_data_table: Dict[str, GatoRobotoItemData] = {
    ItemName.progressive_vent_1: GatoRobotoItemData(gato_roboto_base_id + 262, ItemClassification.progression),
    ItemName.progressive_vent_2: GatoRobotoItemData(gato_roboto_base_id + 263, ItemClassification.progression),
    ItemName.progressive_vent_3: GatoRobotoItemData(gato_roboto_base_id + 264, ItemClassification.progression),
}

item_data_table: Dict[str, GatoRobotoItemData] = {
    **modules_item_data_table, 
    **cartidges_item_data_table,
    **healthkits_item_data_table,
    **heater_events_item_data_table,
    **aqueduct_events_item_data_table,
    **vent_events_item_data_table
}

item_table = {name: data.code for name, data in item_data_table.items()}
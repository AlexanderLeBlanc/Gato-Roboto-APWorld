from typing import Dict, NamedTuple, Optional

from BaseClasses import Location
from .Names import LocationName
from .Names import RegionName

gatoroboto_base_id: int = 10000

class GatoRobotoLocation(Location):
    game = "Gato Roboto"
    
class GatoRobotoLocationData(NamedTuple):
    region: str
    address: Optional[int] = None

healthkit_location_data_table: Dict[str, str] = {
    LocationName.healthkit_1: GatoRobotoLocationData(RegionName.region_1, gatoroboto_base_id + 408),
    LocationName.healthkit_2: GatoRobotoLocationData(RegionName.region_1, gatoroboto_base_id + 1812),
    LocationName.healthkit_3: GatoRobotoLocationData(RegionName.region_2, gatoroboto_base_id + 1014),
    LocationName.healthkit_4: GatoRobotoLocationData(RegionName.region_2, gatoroboto_base_id + 2314),
    LocationName.healthkit_5: GatoRobotoLocationData(RegionName.region_3, gatoroboto_base_id + 405),
    LocationName.healthkit_6: GatoRobotoLocationData(RegionName.region_3, gatoroboto_base_id + 1606),
    LocationName.healthkit_7: GatoRobotoLocationData(RegionName.region_4, gatoroboto_base_id + 417),
    LocationName.healthkit_8: GatoRobotoLocationData(RegionName.region_4, gatoroboto_base_id + 1713),
    LocationName.healthkit_9: GatoRobotoLocationData(RegionName.region_5, gatoroboto_base_id + 915),
    LocationName.healthkit_10: GatoRobotoLocationData(RegionName.region_6, gatoroboto_base_id + 2413),
}

cartridge_location_data_table: Dict[str, str] = {
    LocationName.cartridge_1: GatoRobotoLocationData(RegionName.region_1, gatoroboto_base_id + 710),
    LocationName.cartridge_2: GatoRobotoLocationData(RegionName.region_1, gatoroboto_base_id + 1810),
    LocationName.cartridge_3: GatoRobotoLocationData(RegionName.region_2, gatoroboto_base_id + 1214),
    LocationName.cartridge_4: GatoRobotoLocationData(RegionName.region_2, gatoroboto_base_id + 1413),
    LocationName.cartridge_5: GatoRobotoLocationData(RegionName.region_2, gatoroboto_base_id + 2113),
    LocationName.cartridge_6: GatoRobotoLocationData(RegionName.region_3, gatoroboto_base_id + 1106),
    LocationName.cartridge_7: GatoRobotoLocationData(RegionName.region_3, gatoroboto_base_id + 707),
    LocationName.cartridge_8: GatoRobotoLocationData(RegionName.region_3, gatoroboto_base_id + 2105),
    LocationName.cartridge_9: GatoRobotoLocationData(RegionName.region_4, gatoroboto_base_id + 1119),
    LocationName.cartridge_10: GatoRobotoLocationData(RegionName.region_4, gatoroboto_base_id + 414),
    LocationName.cartridge_11: GatoRobotoLocationData(RegionName.region_4, gatoroboto_base_id + 1915),
    LocationName.cartridge_12: GatoRobotoLocationData(RegionName.region_5, gatoroboto_base_id + 1613),
    LocationName.cartridge_13: GatoRobotoLocationData(RegionName.region_5, gatoroboto_base_id + 517),
    LocationName.cartridge_14: GatoRobotoLocationData(RegionName.region_6, gatoroboto_base_id + 1514),
}

module_location_data_table: Dict[str, str] = {
    LocationName.module_1: GatoRobotoLocationData(RegionName.region_1, gatoroboto_base_id + 814),
    LocationName.module_2: GatoRobotoLocationData(RegionName.region_1, gatoroboto_base_id + 807),
    LocationName.module_3: GatoRobotoLocationData(RegionName.region_2, gatoroboto_base_id + 1716),
    LocationName.module_4: GatoRobotoLocationData(RegionName.region_2, gatoroboto_base_id + 11716),
    LocationName.module_5: GatoRobotoLocationData(RegionName.region_3, gatoroboto_base_id + 2410),
    LocationName.module_6: GatoRobotoLocationData(RegionName.region_4, gatoroboto_base_id + 113),
    LocationName.module_7: GatoRobotoLocationData(RegionName.region_4, gatoroboto_base_id + 1114),
    LocationName.module_8: GatoRobotoLocationData(RegionName.region_5, gatoroboto_base_id + 1718),
}

event_location_data_table: Dict[str, str] = {
    LocationName.aqueduct_1: GatoRobotoLocationData(RegionName.region_3, gatoroboto_base_id + 204),
    LocationName.aqueduct_2: GatoRobotoLocationData(RegionName.region_3, gatoroboto_base_id + 1503),
    LocationName.aqueduct_3: GatoRobotoLocationData(RegionName.region_3, gatoroboto_base_id + 1908),
    LocationName.heater_1: GatoRobotoLocationData(RegionName.region_4, gatoroboto_base_id + 19),
    LocationName.heater_2: GatoRobotoLocationData(RegionName.region_4, gatoroboto_base_id + 313),
    LocationName.heater_3: GatoRobotoLocationData(RegionName.region_4, gatoroboto_base_id + 15),
    LocationName.vent_1: GatoRobotoLocationData(RegionName.region_5, gatoroboto_base_id + 1112),
    LocationName.vent_2: GatoRobotoLocationData(RegionName.region_5, gatoroboto_base_id + 1122),
    LocationName.vent_3: GatoRobotoLocationData(RegionName.region_5, gatoroboto_base_id + 521)
}

location_data_table: Dict[str, str] = {
    **healthkit_location_data_table,
    **cartridge_location_data_table,
    **module_location_data_table,
    **event_location_data_table
}

location_table = {name: data.address for name, data in location_data_table.items()}
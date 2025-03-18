from typing import Dict, List, NamedTuple
from .Names import RegionName

class GatoRobotoRegionData(NamedTuple):
    connecting_regions: List[str] = []
    

region_data_table: Dict[str, GatoRobotoRegionData] = {
    RegionName.region_0: GatoRobotoRegionData([RegionName.region_1]),
    RegionName.region_1: GatoRobotoRegionData([RegionName.region_2]),
    RegionName.region_2: GatoRobotoRegionData([RegionName.region_3, RegionName.region_4, RegionName.region_5, RegionName.region_6]),
    RegionName.region_3: GatoRobotoRegionData(),
    RegionName.region_4: GatoRobotoRegionData(),
    RegionName.region_5: GatoRobotoRegionData(),
    RegionName.region_6: GatoRobotoRegionData([RegionName.region_7]),
    RegionName.region_7: GatoRobotoRegionData()
}
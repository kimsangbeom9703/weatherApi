from crud import crud_get

from db.models.areaModel import AreaDataModel
from db.models.incheonAirportDustDataModel import IncheonAirportDustDataModel
from db.models.incheonAirportDustStationModel import IncheonAirportDustStationModel

def getDustAllData(db):
    return crud_get.getAreaListAllData(db)
def getDustStationAllData(db,page,size):
    return crud_get.get_all_data(db,IncheonAirportDustStationModel,skip=page*size, limit=size)


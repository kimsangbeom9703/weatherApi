from crud import crud_get

from db.models.areaModel import AreaDataModel
from db.models.incheonAirportDustDataModel import IncheonAirportDustDataModel
from db.models.incheonAirportDustStationModel import IncheonAirportDustStationModel

def getAreaAllData(db):
    return crud_get.getAreaListAllData(db)
def getDustStationAllData(db,page,size):
    return crud_get.get_all_data(db,IncheonAirportDustStationModel,skip=page*size, limit=size)

#시간대 별 6개 측정소 데이터 노출
def getDustStationDataByTime(db,current_tiem=None):
    return current_tiem

from sqlalchemy.orm import Session
from db.models.areaModel import AreaDataModel
from db.models.incheonAirportDustDataModel import IncheonAirportDustDataModel
from db.models.incheonAirportDustStationModel import IncheonAirportDustStationModel
def getAreaListAllData(db: Session):
    return db.query(AreaDataModel).all()
def getIncheonDustStationAllData(db:Session):
    return db.query(IncheonAirportDustStationModel).all()
def getIncheonDustDataAllData(db:Session):
    return db.query(IncheonAirportDustDataModel).all()
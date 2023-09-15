from sqlalchemy.orm import Session
from app.db.models.areaModel import AreaData
def getAreaListAllData(db: Session):
    return db.query(AreaData).all()
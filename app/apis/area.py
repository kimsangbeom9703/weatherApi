from crud import crud_get

def listAllData(db):
    areaData = crud_get.getAreaListAllData(db)
    return areaData
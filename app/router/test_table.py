from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..connection import baseModels, models
from ..connection.database import get_db

router = APIRouter(tags=["CRUD Operations"])

@router.get("/")
def root(db: Session = Depends(get_db)):
    return get_item(db)

@router.get("/get")
def get_item(db: Session = Depends(get_db)):
    data = db.query(models.TestTable).all()
    return {"message": "Item get successfully", "data": data}

@router.get("/get/{id}")
def get_item_by_id(id: int, db: Session = Depends(get_db)):
    try:
        data = db.query(models.TestTable).filter(models.TestTable.id == id).first()
        if not data:
            return {"message": "Item not found"}
        return {"message": "Item get successfully", "data": data}
    except Exception as e:
        return {"error": str(e)}

@router.post("/create")
def create_item(test_table: baseModels.TestTableId, db: Session = Depends(get_db)):
    try:
        new_item = models.TestTable(title=test_table.title, body=test_table.body)
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return {"message": "Item created successfully", "data": new_item}
    except Exception as e:
        return {"error": str(e)}

@router.put("/update/{id}")
def update_item(id: int, test_table: baseModels.TestTable, db: Session = Depends(get_db)):
    try:
        item = db.query(models.TestTable).filter(models.TestTable.id == id).first()
        if not item:
            return {"message": "Item not found"}
        item.id = id
        item.title = test_table.title
        item.body = test_table.body
        db.commit()
        db.refresh(item)
        return {"message": "Item updated successfully", "data": item}
    except Exception as e:
        return {"error": str(e)}

@router.delete("/delete/{id}")
def delete_item(id: int, db: Session = Depends(get_db)):
    try:
        item = db.query(models.TestTable).filter(models.TestTableId.id == id).first()
        if not item:
            return {"message": "Item not found"}
        db.delete(item)
        db.commit()
        return {"message": "Item deleted successfully"}
    except Exception as e:
        return {"error": str(e)}
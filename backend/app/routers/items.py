from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from app.database import Session
from app.models import Item
from app.routers.auth import oauth2_scheme

router = APIRouter()

@router.post("/items")
def create_item(title: str, description: str, token: str = Depends(oauth2_scheme)):
    new_item = Item(title=title, description=description)
    Session.add(new_item)
    Session.commit()
    return {"item": new_item}

@router.get("/items")
def get_items(token: str = Depends(oauth2_scheme)):
    items = Session.query(Item).all()
    return {"items": items}

@router.put("/items/{id}")
def update_item(id: int, title: str, description: str, token: str = Depends(oauth2_scheme)):
    item = Session.query(Item).filter_by(id=id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item.title = title
    item.description = description
    Session.commit()
    return {"item": item}

@router.delete("/items/{id}")
def delete_item(id: int, token: str = Depends(oauth2_scheme)):
    item = Session.query(Item).filter_by(id=id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    Session.delete(item)
    Session.commit()
    return {"message": "Item deleted"}
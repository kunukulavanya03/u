from fastapi import APIRouter, Depends, HTTPException
from app.config import settings
from app.models import Resource
from app.utils import get_user

router = APIRouter()

@router.get("/resources")
def get_resources(user: User = Depends(get_user)):
    resources = Resource.query.filter_by(user_id=user.id).all()
    return [{"resource_id": resource.id, "name": resource.name, "description": resource.description} for resource in resources]
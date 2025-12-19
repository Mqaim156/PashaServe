from ..main import app
from fastapi import APIRouter

router = APIRouter()

@router.get("/api/campaigns")
def campaigns():
    return "Campaigns"
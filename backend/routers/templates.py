from ..main import app
from fastapi import APIRouter

router = APIRouter()

@router.get("/api/templates")
def templates():
    return "Templates"
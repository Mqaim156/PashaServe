from fastapi import APIRouter

router = APIRouter()

@router.get("/api/customers")
def customers():
    return "Customers"
from fastapi import APIRouter, Query
from services.clv_service import compute_clv_report
from models.responses import CLVReport

router = APIRouter(prefix="/api/clv", tags=["clv"])

@router.get("/report", response_model=CLVReport)
def clv_report(user: str = Query(...)):
    return compute_clv_report(user)

from fastapi import APIRouter, Query
from services.odds_service import get_odds, get_sports, OddsAPIError

router = APIRouter(prefix="/api/odds", tags=["odds"])

@router.get("/sports")
def sports():
    try:
        return get_sports()
    except OddsAPIError as e:
        return {"error": str(e)}

@router.get("")
def odds(sport_key: str = Query("basketball_nba")):
    try:
        return get_odds(sport_key)
    except OddsAPIError as e:
        return {"error": str(e)}

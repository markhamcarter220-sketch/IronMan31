from pydantic import BaseModel

class Bet(BaseModel):
    user: str
    matchup: str
    sportsbook: str
    odds: float
    stake: float
    closing_odds: float | None = None

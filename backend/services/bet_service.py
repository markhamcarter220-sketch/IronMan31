from db.mongo import get_bets_collection
from models.bet import Bet
import uuid

def log_bet(bet: Bet):
    clv = round((bet.odds - bet.closing_odds) / abs(bet.closing_odds), 3) if bet.closing_odds else None
    bet_dict = bet.dict()
    bet_dict["clv"] = clv
    bet_dict["id"] = str(uuid.uuid4())
    get_bets_collection().insert_one(bet_dict)
    return bet_dict

def fetch_bets(user: str):
    return list(get_bets_collection().find({"user": user}, {"_id": 0}))

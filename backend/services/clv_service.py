from db.mongo import get_bets_collection

def compute_clv_report(user: str) -> dict:
    bets = list(get_bets_collection().find({"user": user, "clv": {"$ne": None}}, {"_id": 0, "clv": 1}))
    total = len(bets)
    if total == 0:
        return {
            "user": user,
            "total_bets": 0,
            "avg_clv": 0.0,
            "clv_positive_rate": 0.0,
            "max_clv": 0.0,
            "min_clv": 0.0,
            "positive_bets": 0,
            "negative_bets": 0
        }
    clvs = [b["clv"] for b in bets]
    pos = [c for c in clvs if c > 0]
    neg = [c for c in clvs if c < 0]
    return {
        "user": user,
        "total_bets": total,
        "avg_clv": round(sum(clvs) / total, 4),
        "clv_positive_rate": round(len(pos) / total, 3),
        "max_clv": max(clvs),
        "min_clv": min(clvs),
        "positive_bets": len(pos),
        "negative_bets": len(neg)
    }

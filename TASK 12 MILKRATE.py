"""Rate card v2: Decimal arithmetic, season parameter, 2-decimal readings, bonus."""
from decimal import Decimal as D, ROUND_HALF_UP

Q = D("0.01")
STD_FAT, STD_SNF, STEP = D("3.5"), D("8.5"), D("0.1")
BONUS_LIMIT, BONUS_PER_LITRE = D("500"), D("0.50")

RATE_CARDS = {   # all seasonal numbers live here
    "regular": {"base": D("30.00"), "fat": D("0.40"), "snf": D("0.30")},
    "summer":  {"base": D("32.00"), "fat": D("0.45"), "snf": D("0.30")},  # Apr-Jun
}


def season_for(month):
    """Returns 'summer' for April-June (4-6), otherwise 'regular'."""
    return "summer" if 4 <= month <= 6 else "regular"


def rate_per_litre(fat, snf, season="regular"):
    """Rate per litre; steps are fractional (pro-rata) so 4.24 % differs from 4.20 %."""
    card = RATE_CARDS[season]
    fat_steps = (D(str(fat)) - STD_FAT) / STEP
    snf_steps = (D(str(snf)) - STD_SNF) / STEP
    return (card["base"] + fat_steps * card["fat"] + snf_steps * card["snf"]).quantize(Q, ROUND_HALF_UP)


def payout(litres, fat, snf, season="regular"):
    """Amount for one entry."""
    return (D(str(litres)) * rate_per_litre(fat, snf, season)).quantize(Q, ROUND_HALF_UP)


def bonus(total_litres):
    """Rs 0.50 per litre on ALL litres when ten-day supply exceeds 500 L, else 0."""
    t = D(str(total_litres))
    return (t * BONUS_PER_LITRE).quantize(Q, ROUND_HALF_UP) if t > BONUS_LIMIT else D("0.00")


def ten_day_total(entries, season="regular"):
    """entries: [(litres, fat, snf)]. Returns (payments, bonus, grand total)."""
    pay = sum((payout(l, f, s, season) for l, f, s in entries), D("0"))
    lit = sum((D(str(l)) for l, _, _ in entries), D("0"))
    b = bonus(lit)
    return pay, b, pay + b

"""Task 11 - Generate milk-rate values in JSON format."""
import json
 
RATE_CARD = {
    "base": 30.0,
    "fat": 0.40,
    "snf": 0.30
}
 
def calculate_rate(fat, snf):
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
 
    rate = RATE_CARD["base"] + fat_steps * RATE_CARD["fat"] + snf_steps * RATE_CARD["snf"]
    return round(rate, 2)
 
for fat, snf in [(3.5, 8.5), (4.2, 8.7), (3.1, 8.3)]:
    print("Rate:", calculate_rate(fat, snf))

"""Task 12 - Calculate seasonal milk payment using functions."""
def rate(fat, snf, season):
    base = 30
    fat_value = 0.40
 
    if season == "summer":
        base = 32
        fat_value = 0.45
 
    fat_steps = round((fat - 3.5) * 10)
    snf_steps = round((snf - 8.5) * 10)
 
    return base + fat_steps * fat_value + snf_steps * 0.30
 
 
def payout(litres, fat, snf, season):
    amount = litres * rate(fat, snf, season)
 
    if season == "summer" and litres > 500:
        amount = amount + litres * 0.50
 
    return round(amount, 2)
 
 
for litres, fat, snf in [(10, 3.50, 8.50), (600, 4.20, 8.70)]:
    print("Payment:", payout(litres, fat, snf, "summer"))
 

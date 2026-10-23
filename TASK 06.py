"""Task 6 - Calculate the total payout for ten milk entries using functions."""
BASE_RATE = 30.0
FAT_VALUE = 0.40
SNF_VALUE = 0.30
 
def rate_per_litre(fat, snf):
    """Calculate milk rate."""
    return round(30 + round((fat-3.5)/0.1)*FAT_VALUE
                 + round((snf-8.5)/0.1)*SNF_VALUE, 2)
 
def payout(litres, fat, snf):
    """Calculate payment."""
    return round(litres * rate_per_litre(fat, snf), 2)
 
def ten_day_total():
    """Calculate 10-day total."""
    total = 0
    for i in range(10):
        litres = float(input("Litres: "))
        fat = float(input("Fat: "))
        snf = float(input("SNF: "))
        total += payout(litres, fat, snf)
    return round(total, 2)
 
print("Total payment:", ten_day_total())

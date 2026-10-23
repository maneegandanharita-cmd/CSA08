"""Task 4 - Display milk rates for different fat percentages."""
BASE_RATE = 30.0
FAT_VALUE = 0.40
SNF_VALUE = 0.30
 
for fat in [4.2, 3.1, 3.5]:
    fat_steps = round((fat - 3.5) / 0.1)
 
    rate = BASE_RATE + fat_steps * FAT_VALUE
 
    print("Fat:", fat)
    print("Fat steps:", fat_steps)
    print("Milk rate:", round(rate, 2))
    print()

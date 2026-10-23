"""Task 3 - Calculate milk rate from entered fat and SNF values."""
BASE_RATE = 30.0
FAT_VALUE = 0.40
SNF_VALUE = 0.30
 
for i in range(1, 4):
    fat = float(input("Enter fat: "))
    snf = float(input("Enter SNF: "))
 
    rate = BASE_RATE + ((fat - 3.5) / 0.1) * FAT_VALUE + ((snf - 8.5) / 0.1) * SNF_VALUE
 
    print("Milk rate =", round(rate, 2))

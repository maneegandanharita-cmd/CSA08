"""Task 1 - Calculate milk payment for farmers using litres, fat and SNF."""
DAYS = 10
 
n = int(input("Enter number of farmers: "))
 
for i in range(n):
    farmer_id = input("Enter farmer ID: ")
    litres = float(input("Enter litres of milk: "))
    fat = float(input("Enter fat percentage: "))
    snf = float(input("Enter SNF percentage: "))
    shift = input("Enter shift (Morning/Evening): ")
 
    if litres < 0 or fat < 2 or fat > 7 or snf < 0 or snf > 15:
        print("Invalid data")
    else:
        rate = (fat * 5) + (snf * 2)
        amount = litres * rate
        total = amount * DAYS
 
        print("Farmer ID:", farmer_id)
        print("Shift:", shift)
        print("Rate per litre: Rs.", rate)
        print("Payment amount: Rs.", amount)
        print("Ten-day total: Rs.", total)

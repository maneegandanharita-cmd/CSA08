"""Task 9 - Calculate total milk payment with validation and error handling."""
BASE_RATE = 30.0
 
total = 0
 
for i in range(1, 6):
    try:
        litres = float(input("Enter litres: "))
        fat = float(input("Enter fat: "))
        snf = float(input("Enter SNF: "))
 
        if litres < 0 or fat < 0 or not (0 <= fat <= 10):
            print("Invalid input")
            continue
 
        fat_steps = round((fat - 3.5) / 0.1)
        snf_steps = round((snf - 8.5) / 0.1)
 
        rate = BASE_RATE + fat_steps * 0.40 + snf_steps * 0.30
        payment = round(litres * rate, 2)
 
        total += payment
        print("Rate:", round(rate, 2))
        print("Payment:", payment)
 
    except ValueError:
        print("Enter numbers only")
 
print("Total payment:", round(total, 2))

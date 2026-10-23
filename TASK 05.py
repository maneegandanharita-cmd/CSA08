"""Task 5 - Calculate milk payment for three entries with input-error handling."""
for i in range(1, 4):
    try:
        litres = float(input("Enter litres: "))
        fat = float(input("Enter fat: "))
        snf = float(input("Enter SNF: "))
 
        rate = 30 + round((fat - 3.5) / 0.1) * 0.40 + round((snf - 8.5) / 0.1) * 0.30
        amount = litres * rate
 
        print(f"Amount to pay: Rs. {amount:8.2f}")
 
    except ValueError:
        print("Invalid input! Enter numbers only.")

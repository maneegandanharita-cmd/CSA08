"""Task 8 - Calculate and total milk payments for ten days."""
total = 0
 
for i in range(1, 11):
    litres = float(input("Enter litres: "))
    fat = float(input("Enter fat: "))
    snf = float(input("Enter SNF: "))
 
    rate = 30 + round((fat - 3.5) / 0.1) * 0.40 + round((snf - 8.5) / 0.1) * 0.30
 
    payment = litres * rate
    total = total + payment
 
    print("Payment:", round(payment, 2))
 
print("Total 10-day payment:", round(total, 2))

      

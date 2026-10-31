"""Task 8 - Calculate and total milk payments for ten days."""
total=0

for i in range (1,11):
 litres = float(input("enter litres: ")
 fat = float(input("enter fat: ")
 snf = float(input("enter snf:" )

 rate=30 + round(fat-3.5)/0.1) * 0.40 + round((snf-8.5)/0.1) *0.3

 payment=litres +rate
 total = total + payment

 print('payment:", round(payment, 2))

print("total 10-day payment",round9total,2))
      

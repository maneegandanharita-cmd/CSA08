"""Task 10 - Compare floating-point and Decimal totals and measure execution time."""
import time
from decimal import Decimal
 
for n in [300, 6000, 150000]:
    start = time.perf_counter()
 
    float_total = 0.1 * n
    decimal_total = Decimal("0.10") * n
 
    end = time.perf_counter()
 
    print("Payments:", n)
    print("Float total:", round(float_total, 2))
    print("Decimal total:", decimal_total)
    print("Time:", round(end - start, 6), "seconds")

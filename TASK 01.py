"""Task 1 - alternative design: separate variables vs one tuple per entry."""
import sys, time

# Design A: 3 variables per farmer. For 3 farmers the code already looks like this,
# and for 300 farmers it would need 900 names and 300 copies of the formula.
litres1, fat1, snf1 = 10, 3.5, 8.5
litres2, fat2, snf2 = 8.5, 4.2, 8.7
litres3, fat3, snf3 = 12, 3.1, 8.3
# ... litres300, fat300, snf300 ...  (impossible to loop over)

# Design B: list of tuples - one loop handles any n.
def total(entries):
    t = 0.0
    for litres, fat, snf in entries:
        t += litres * (30 + round((fat - 3.5) / 0.1) * 0.4 + round((snf - 8.5) / 0.1) * 0.3)
    return round(t, 2)

for n in (300, 3000, 30000):
    entries = [(10, 3.5, 8.5)] * n
    s = time.perf_counter(); total(entries); e = time.perf_counter()
    print(f"n={n:6}  time={e - s:.6f}s  list+tuples size={sys.getsizeof(entries)} bytes (list only)")
print("Design A source size for 300 farmers ~ 300 x 3 assignments + 300 formula lines = 1200 lines")

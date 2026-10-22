"""Task 8 alternative: store list vs running total; verifies the hand trace."""
import sys, os, tracemalloc
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "task07_module"))
from milkrate import payout

entries = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]
total = 0.0
for l, f, s in entries:
    total += payout(l, f, s)
    print(f"{l:5} {f} {s}  -> running total {total:.2f}")
print("Hand trace total = 917.50, program total =", round(total, 2))

n = 200000
tracemalloc.start()
stored = [payout(10, 3.5, 8.5) for _ in range(n)]; sum(stored)
print("store-all peak bytes :", tracemalloc.get_traced_memory()[1]); tracemalloc.stop()
tracemalloc.start()
run = 0.0
for _ in range(n): run += payout(10, 3.5, 8.5)
print("running-total peak   :", tracemalloc.get_traced_memory()[1]); tracemalloc.stop()

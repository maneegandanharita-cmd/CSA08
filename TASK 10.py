"""Task 10 - float vs Decimal, timing, round-each vs round-total, rate table."""
import sys, os, random, time
from decimal import Decimal, ROUND_HALF_UP
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "task07_module"))
from milkrate import rate_per_litre

random.seed(42)
Q = Decimal("0.01")


def make(n):
    return [(Decimal(random.randint(50, 400)) / 10, round(random.uniform(3.0, 5.0), 1),
             round(random.uniform(8.0, 9.0), 1)) for _ in range(n)]


for n in (300, 6000, 150000):
    data = make(n)
    t0 = time.perf_counter()
    f_each = sum(round(float(l) * rate_per_litre(f, s), 2) for l, f, s in data)
    t1 = time.perf_counter()
    exact_each = Decimal(0); exact_raw = Decimal(0)
    for l, f, s in data:
        raw = l * Decimal(str(rate_per_litre(f, s)))
        exact_raw += raw
        exact_each += raw.quantize(Q, ROUND_HALF_UP)
    t2 = time.perf_counter()
    print(f"n={n:6} float(sum of rounded)={f_each:.6f} Decimal(each rounded)={exact_each} "
          f"Decimal(round total)={exact_raw.quantize(Q, ROUND_HALF_UP)}")
    print(f"         |float-Decimal|={abs(Decimal(f_each) - exact_each):.10f}  "
          f"round-each vs round-total diff={exact_each - exact_raw.quantize(Q, ROUND_HALF_UP)}  "
          f"time float={t1 - t0:.4f}s Decimal={t2 - t1:.4f}s")

# alternative: rate table
data = make(150000)
t = time.perf_counter(); [rate_per_litre(f, s) for _, f, s in data]; a = time.perf_counter() - t
table = {}
t = time.perf_counter()
for _, f, s in data:
    k = (f, s)
    if k not in table:
        table[k] = rate_per_litre(f, s)
    table[k]
b = time.perf_counter() - t
print(f"recalculate: {a:.4f}s | rate-table: {b:.4f}s | distinct pairs k={len(table)}")

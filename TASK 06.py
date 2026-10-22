"""Task 6 - functions, scope, docstrings; script vs lambda alternative."""
import sys, os, timeit
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "task07_module"))
from milkrate import rate_per_litre, payout


def ten_day_total(entries):
    """Returns the sum of payouts for entries [(litres, fat, snf), ...] rounded to 2 decimals."""
    total = 0.0
    for litres, fat, snf in entries:
        total += payout(litres, fat, snf)
    return round(total, 2)


def show_payout(litres, fat, snf):
    """PRINTS (returns None) - contrast with payout() which RETURNS."""
    print(payout(litres, fat, snf))


def bad_scope():
    """Assigning to a name makes it local; the global BASE_RATE stays unchanged."""
    BASE_RATE = 0
    return BASE_RATE


entries = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]
print("ten_day_total:", ten_day_total(entries))
r = show_payout(10, 3.5, 8.5)
print("show_payout returned:", r)
print("bad_scope() =", bad_scope(), "| milkrate.BASE_RATE still", __import__("milkrate").BASE_RATE)

# alternative: lambda / inline script
lam = lambda l, f, s: round(l * (30 + round((f - 3.5) / .1) * .4 + round((s - 8.5) / .1) * .3), 2)
print("lambda result:", lam(8.5, 4.2, 8.7))
n = 100000
t1 = timeit.timeit(lambda: payout(8.5, 4.2, 8.7), number=n)
t2 = timeit.timeit(lambda: lam(8.5, 4.2, 8.7), number=n)
print(f"function-call overhead: payout {t1:.4f}s vs lambda {t2:.4f}s for {n} calls")

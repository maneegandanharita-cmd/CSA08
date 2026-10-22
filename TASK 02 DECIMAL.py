"""Task 2 - Complete the Code (TODO 1) + alternatives."""
import sys, time
from decimal import Decimal

payments = ["33.40"] * 1000 + ["0.10"] * 3


def total_float(items):
    total = 0.0
    for amount in items:
        total += float(amount)
    return total


def total_decimal(items):
    total = Decimal("0")
    for amount in items:
        total += Decimal(amount)          # TODO 1 solved
    return total


def total_decimal_from_float(items):      # the "change" asked in the task
    total = Decimal("0")
    for amount in items:
        total += Decimal(float(amount))
    return total


def total_paise(items):                   # alternative 1: integer paise
    total = 0
    for amount in items:
        rupees, paise = amount.split(".")
        total += int(rupees) * 100 + int(paise)
    return total


def total_float_round(items):             # alternative 2: float + round each step
    total = 0.0
    for amount in items:
        total = round(total + float(amount), 2)
    return total


print("float  :", total_float(payments))
print("Decimal:", total_decimal(payments))
print(0.1 + 0.2 == 0.3, Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
print()
print("--- extra evidence ---")
print("Decimal(float(amount)):", total_decimal_from_float(payments))
print("Decimal(33.40)        :", Decimal(33.40))
p = total_paise(payments)
print("integer paise         :", p, "->", f"Rs {p // 100}.{p % 100:02d}")
print("float + round()       :", total_float_round(payments))
print("sizeof float / int / Decimal:", sys.getsizeof(1.5), sys.getsizeof(3340), sys.getsizeof(Decimal("33.40")))
for f in (total_float, total_decimal, total_paise, total_float_round):
    big = payments * 100
    s = time.perf_counter(); f(big); e = time.perf_counter()
    print(f"{f.__name__:20} {len(big)} items: {e - s:.5f}s")

"""Task 4 - expressions and surprises."""
import math
print("(4.2 - 3.5) / 0.1      =", (4.2 - 3.5) / 0.1)
print("round((4.2-3.5)/0.1)   =", round((4.2 - 3.5) / 0.1))
print("-2 ** 2                =", -2 ** 2, "  (** binds tighter than unary minus)")
print("2 ** 3 ** 2            =", 2 ** 3 ** 2, " (** is right-associative)")
print("round(2.5), round(3.5) =", round(2.5), round(3.5), " (banker's rounding)")
print("round(-2.5)            =", round(-2.5))
print("int(-2.7), math.floor(-2.7), round(-2.7) =", int(-2.7), math.floor(-2.7), round(-2.7))
print("1.1 * 3                =", 1.1 * 3)
fat = 4.5
print("2.0 <= fat <= 7.0      =", 2.0 <= fat <= 7.0)
print("True and not False or False =", True and not False or False)

print("\nAlternative step counting (base 30, fat 0.40, snf at standard):")
for fat in (4.2, 3.1):
    exact = (fat - 3.5) / 0.1
    r, i, f = round(exact), int(exact), math.floor(exact)
    rate = lambda s: round(30 + s * 0.40, 2)
    print(f"fat={fat}: exact={exact!r:22} round->{r:3} rate {rate(r)} | int->{i:3} rate {rate(i)} | floor->{f:3} rate {rate(f)}")

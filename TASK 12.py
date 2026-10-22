"""Task 12 tests + evidence that the OLD design is wrong for 2-decimal readings."""
import sys, os
from decimal import Decimal as D
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "task07_module"))
import milkrate as old
import milkrate_v2 as new

print("Old design with 2-decimal readings (fat 4.24 vs 4.20, same rate = wrong):")
print("  old rate(4.24, 8.5) =", old.rate_per_litre(4.24, 8.5), " old rate(4.20, 8.5) =", old.rate_per_litre(4.20, 8.5))
print("  new rate(4.24, 8.5) =", new.rate_per_litre("4.24", "8.5"), " new rate(4.20, 8.5) =", new.rate_per_litre("4.20", "8.5"))

tests = [
    ("regular standard", new.rate_per_litre("3.5", "8.5", "regular"), D("30.00")),
    ("regular 4.2/8.7",  new.rate_per_litre("4.2", "8.7", "regular"), D("33.40")),
    ("summer standard",  new.rate_per_litre("3.5", "8.5", "summer"), D("32.00")),
    ("summer 4.2/8.7",   new.rate_per_litre("4.2", "8.7", "summer"), D("32.00") + 7 * D("0.45") + 2 * D("0.30")),
    ("regular 4.24/8.53",new.rate_per_litre("4.24", "8.53", "regular"), D("30.00") + D("7.4") * D("0.40") + D("0.3") * D("0.30")),
    ("bonus 500 L (no)", new.bonus(500), D("0.00")),
    ("bonus 500.5 L",    new.bonus("500.5"), D("250.25")),
    ("season Apr", new.season_for(4), "summer"), ("season Jul", new.season_for(7), "regular"),
]
print(f"\n{'Case':20}{'Expected':>12}{'Actual':>12}")
for name, act, exp in tests:
    assert act == exp, (name, act, exp)
    print(f"{name:20}{str(exp):>12}{str(act):>12}  PASS")

entries = [(300, 3.5, 8.5), (250, 4.2, 8.7)]           # 550 L -> bonus applies
for season in ("regular", "summer"):
    p, b, g = new.ten_day_total(entries, season)
    print(f"{season:8} payments={p} bonus={b} grand total={g}")
assert new.ten_day_total(entries, "regular")[1] == D("275.00")
print("ALL TASK 12 TESTS PASSED")

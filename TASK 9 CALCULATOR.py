"""Task 9 - assert-based tests + printed table."""
from calculator import entry_payout

valid = [
    ("standard",        (10, 3.5, 8.5), 300.00),
    ("fat above",       (10, 4.0, 8.5), 320.00),
    ("fat below",       (10, 3.0, 8.5), 280.00),
    ("snf above",       (10, 3.5, 9.0), 315.00),
    ("snf below",       (10, 3.5, 8.0), 285.00),
    ("lowest fat 2.0",  (10, 2.0, 8.5), 240.00),
    ("highest fat 7.0", (10, 7.0, 8.5), 440.00),
    ("zero litres",     (0, 3.5, 8.5), 0.00),
    ("sample 1",        (8.5, 4.2, 8.7), 283.90),
    ("sample 2",        (12, 3.1, 8.3), 333.60),
]
invalid = [("text litres", ("eight", 3.5, 8.5)), ("negative litres", (-5, 3.5, 8.5)),
           ("fat 1.9", (10, 1.9, 8.5)), ("fat 7.1", (10, 7.1, 8.5)), ("comma 8,5", ("8,5", 3.5, 8.5))]

print(f"{'Case':18}{'Expected':>10}{'Actual':>10}  Result")
for name, args, exp in valid:
    act = entry_payout(*args)
    assert act == exp, (name, act, exp)
    print(f"{name:18}{exp:10.2f}{act:10.2f}  PASS")
for name, args in invalid:
    try:
        entry_payout(*args); raise AssertionError(name)
    except ValueError as e:
        print(f"{name:18}{'ValueError':>10}{'ValueError':>10}  PASS ({e})")

# hand-calculated set of 5: 300 + 283.90 + 333.60 + 320.00 + 280.00 = 1517.50
five = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3), (10, 4.0, 8.5), (10, 3.0, 8.5)]
total = round(sum(entry_payout(*e) for e in five), 2)
assert total == 1517.50
print("5-entry total expected 1517.50 actual", total, "PASS")
print("ALL TESTS PASSED")

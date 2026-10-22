"""Task 9 - complete calculator with validation."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "task07_module"))
from milkrate import payout, MIN_FAT, MAX_FAT


def parse(text):
    t = str(text).strip()
    if t.lstrip("-").replace(".", "", 1).isdigit() and t.count("-") <= 1 and t.find("-") <= 0:
        return float(t)
    raise ValueError(f"not a valid number: {text!r}")


def validate(litres, fat, snf):
    l, f, s = parse(litres), parse(fat), parse(snf)
    if l < 0:
        raise ValueError("litres cannot be negative")
    if not MIN_FAT <= f <= MAX_FAT:
        raise ValueError("fat must be between 2.0 and 7.0")
    if s <= 0:
        raise ValueError("snf must be positive")
    return l, f, s


def entry_payout(litres, fat, snf):
    l, f, s = validate(litres, fat, snf)
    return payout(l, f, s)


def main():
    farmer = input("Farmer ID: ")
    total = 0.0
    for day in range(1, 11):
        for shift in ("M", "E"):
            try:
                a = entry_payout(input(f"Day {day} {shift} litres: "), input("  fat %: "), input("  snf %: "))
                print(f"  amount {a:8.2f}")
                total += a
            except ValueError as e:
                print("  rejected:", e)
    print(f"Farmer {farmer} ten-day total: {total:10.2f}")


if __name__ == "__main__":
    main()

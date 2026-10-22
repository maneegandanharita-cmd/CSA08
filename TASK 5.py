"""Task 5 - reading input, validation and formatted output."""
import timeit


def is_valid_number(text):
    """String-method check: optional spaces, digits, at most one dot."""
    t = text.strip()
    if t.count(".") > 1 or t == "" or t == ".":
        return False
    return t.replace(".", "", 1).isdigit()


def parse_try(text):
    """try/except alternative."""
    try:
        return float(text)
    except ValueError:
        return None


def read_float(prompt):
    while True:
        text = input(prompt)
        if is_valid_number(text):
            return float(text)
        print("  invalid number, try again")


if __name__ == "__main__":
    for s in ["8.5", " 8.5 ", "8,5", "eight", "-3", "1e2", "8..5", ""]:
        print(f"{s!r:10} string-check={str(is_valid_number(s)):5}  try/except={parse_try(s)}")
    print("\nTiming 100000 calls on '8.5':")
    print(" string check:", round(timeit.timeit(lambda: is_valid_number("8.5"), number=100000), 4))
    print(" try/except  :", round(timeit.timeit(lambda: parse_try("8.5"), number=100000), 4))
    amount = 283.9
    print(f"\n|{amount:8.2f}| |{'Rs':>4}| |{12:5}| |{4.2:<6.1f}|")

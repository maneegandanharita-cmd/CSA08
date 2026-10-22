"""Task 3 - named constants, dynamic typing, multiple assignment."""
BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
STD_FAT, STD_SNF = 3.5, 8.5
MIN_FAT, MAX_FAT = 2.0, 7.0

x = 10
print("x =", x, type(x))
x = "ten"                     # dynamic typing: same name, new type
print("x =", x, type(x))

a, b = 3.5, 8.5
a, b = b, a                   # swap without temp variable
print("after swap:", a, b)

BASE_RATE = 99                # Python allows this! UPPER_CASE is only a convention
print("constant changed by mistake ->", BASE_RATE)

RATE_CARD = {"base": 30.0, "fat": 0.40, "snf": 0.30}   # alternative design
print("dict alternative:", RATE_CARD["base"] + 2 * RATE_CARD["fat"])

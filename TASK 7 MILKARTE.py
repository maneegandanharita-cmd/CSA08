"""Second script that imports milkrate (Task 7)."""
import milkrate
from milkrate import payout
import milkrate as mr
import sys

print("__name__ of milkrate when imported:", milkrate.__name__)
print("payout(8.5, 4.2, 8.7)      =", payout(8.5, 4.2, 8.7))
print("milkrate.rate_per_litre    =", milkrate.rate_per_litre(3.1, 8.3))
print("mr.BASE_RATE               =", mr.BASE_RATE)
print("'milkrate' in sys.modules  =", "milkrate" in sys.modules)
print("sys.path[0] (searched 1st) =", sys.path[0])
# Note: the demo table of milkrate.py was NOT printed above, because of the
# `if __name__ == "__main__":` guard.

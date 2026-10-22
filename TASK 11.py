"""Task 11 alternative - rate card read from JSON at start-up."""
import json, os, time
path = os.path.join(os.path.dirname(__file__), "rates.json")
t = time.perf_counter()
with open(path) as fh:
    rates = json.load(fh)
print("loaded", rates, f"in {time.perf_counter() - t:.6f}s")

# Milk Co-operative Payment Calculator - Assignment

Python solution for the village milk co-operative payment problem (Tasks 1-12).

**Name:** <your name>  **Reg. No:** <your reg no>  **Course:** <course code>

## Structure
| Folder | Task | Run |
|---|---|---|
| task01_analysis | 1 - problem analysis, 300-farmer scaling | `python task1_scaling.py` |
| task02_values_types | 2 - types, `/ // %`, float vs Decimal (TODO 1) | `python session.py`, `python task2_decimal.py` |
| task03_constants | 3 - constants, dynamic typing, swapping | `python constants_demo.py` |
| task04_expressions | 4 - precedence, rounding surprises | `python expressions_demo.py` |
| task05_input | 5 - input validation, f-strings | `python input_handling.py` |
| task06_functions | 6 - functions and scope | `python functions_demo.py` |
| task07_module | 7 - `milkrate.py` module (TODO 1, 2) | `python milkrate.py`, `python use_milkrate.py` |
| task08_algorithm | 8 - pseudocode, flowchart, trace | `python running_vs_list.py` |
| task09_testing | 9 - calculator and assert tests | `python test_calculator.py` |
| task10_comparison | 10 - float vs Decimal, timing, rate table | `python compare.py` |
| task11_recommendation | 11 - JSON rate card alternative | `python load_rates.py` |
| task12_design_challenge | 12 - seasonal rates, 2-dp readings, bonus | `python test_v2.py` |

`outputs/` holds the text output of every run. Add screenshots of your own terminal runs to `screenshots/`.
Requires Python 3.8+ and no third-party packages.

## Task 12 design decision (summary)
Modified, not redesigned: constants moved into `RATE_CARDS` keyed by season, `Decimal` arithmetic,
fractional (pro-rata) steps for two-decimal readings, and a separate `bonus()` function.

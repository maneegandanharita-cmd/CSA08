"""Task 2 - reproduces the interactive session (>>> style)."""
import sys
exprs = ['type(10)', 'type(10.0)', 'type("10")', 'type(True)', 'type([10, 8.5])',
         '7 / 2', '7 // 2', '7 % 2', '-7 // 2', '0.1 + 0.2', '0.1 + 0.2 == 0.3',
         'round(0.1 + 0.2, 2) == 0.3', 'isinstance(True, int)', 'True + True']
for e in exprs:
    print(">>>", e)
    print(eval(e))

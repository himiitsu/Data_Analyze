from sympy import *

# ---- ВАШ КОД ТУТ ---

def task_7():
    m = 5
    n = 5
    x = factorial(n)/factorial(n-m)
    y = ((factorial(4)/factorial(n-4))/x)
    print(y)
    return y


# --------------------

proba = task_7()

import unittest


class TestNotebook(unittest.TestCase):
    def test_task(self):
        self.assertAlmostEqual(task_7(), 0.2, places=2)

unittest.main(argv=[''], verbosity=2, exit=False)
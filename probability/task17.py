from sympy import *

# ---- ВАШ КОД ТУТ ---

def C(k, n):
    ret = factorial(n)/(factorial(n-k)*factorial(k))

    return ret

def task_17():
    n = 10**6
    x = C(5,32)-C(1,6)*C(5,22)+C(2,6)*C(5,12)
    return x/n


# --------------------

proba = task_17()

import unittest


class TestNotebook(unittest.TestCase):
    def test_task(self):
        self.assertAlmostEqual(task_17(), 0.055252, places=4)

unittest.main(argv=[''], verbosity=2, exit=False)
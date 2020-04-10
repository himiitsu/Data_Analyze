from sympy import *

# ---- ВАШ КОД ТУТ ---

def A(k, n):
    ret = factorial(n)/(factorial(n-k))

    return ret


def task_14():

    return A(5,5)/A(5,30)
# --------------------

proba = task_14()


import unittest


class TestNotebook(unittest.TestCase):
    def test_task(self):
        self.assertAlmostEqual(task_14(), 0.000007017, places=9)

unittest.main(argv=[''], verbosity=2, exit=False)
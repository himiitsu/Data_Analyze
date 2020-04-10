from sympy import *

# ---- ВАШ КОД ТУТ ---
def task_6_1():
    m = 0
    n = 3
    sub = (subfactorial(n-m)/factorial(n-m) * 1/factorial(m))
    print(f'1, {sub}')
    return sub

def task_6_2():
    m = 1
    n = 3
    sub = (subfactorial(n-m)/factorial(n-m) * 1/factorial(m))
    print(f'2, {sub}')
    return sub

def task_6_3():
    m = 2
    n = 3
    sub = (subfactorial(n-m)/factorial(n-m) * 1/factorial(m))
    print(f'3, {sub}')
    return sub

# --------------------

proba = task_6_1()

proba = task_6_2()

proba = task_6_3()

import unittest


class TestNotebook(unittest.TestCase):
    def test_task(self):
        self.assertAlmostEqual(task_6_1(), 0.296, places=3)
        self.assertAlmostEqual(task_6_2(), 0.148, places=3)
        self.assertAlmostEqual(task_6_3(), 0.074, places=3)

unittest.main(argv=[''], verbosity=2, exit=False)
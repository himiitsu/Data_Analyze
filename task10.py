from sympy import *

# ---- ВАШ КОД ТУТ ---



def C(k, n):
    ret = factorial(n)/(factorial(n-k)*factorial(k))

    return ret


def task_10_1():
    m = 1
    n = 1
    x = (C(3, 6)*C(3, 43))/C(6,49)
    print(f'1, {x}')
    return x


def task_10_2():
    m = 1
    n = 1
    x=(C(0,6)*C(6,43))/C(6,49)
    print(f'2, {1-x}')
    return 1-x


# --------------------

proba = task_10_1()
proba = task_10_2()


import unittest


class TestNotebook(unittest.TestCase):
    def test_task(self):
        self.assertAlmostEqual(task_10_1(), 0.00000143, places=8)
        self.assertAlmostEqual(task_10_2(), 0.00000143, places=8)

unittest.main(argv=[''], verbosity=2, exit=False)


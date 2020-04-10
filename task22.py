from sympy import *

# ---- ВАШ КОД ТУТ ---

def C(k, n):
    ret = factorial(n) / (factorial(n - k) * factorial(k))
    return ret

def task_22(k,n):
    p = 0.1
    x = C(k,n)*(p**k)*((1-p)**(n-k))
    return 1-x


# --------------------

proba = task_22(0,5)
print(f'p={proba:.5f}')

import unittest

#Ошибка в юнит-тесте?
class TestNotebook(unittest.TestCase):
    def test_task(self):
        self.assertAlmostEqual(task_22(), 0.99955, places=5)

unittest.main(argv=[''], verbosity=2, exit=False)
from sympy import *

# ---- ВАШ КОД ТУТ ---

def C(k, n):
    ret = factorial(n) / (factorial(n - k) * factorial(k))
    return ret

def task_21(k,n):
    p = 0.5
    x = C(k,n)*(p**k)*((1-p)**(n-k))
    return x



# --------------------

proba1 = task_21(3,4)

proba2 = task_21(5,8)


print(f'p1 > p2: {proba1, proba2}')

import unittest


class TestNotebook(unittest.TestCase):
    def test_task(self):
        self.assertAlmostEqual(task_21(3,4), 0.25, places=2)
        self.assertAlmostEqual(task_21(5,8), 0.21875, places=5)

unittest.main(argv=[''], verbosity=2, exit=False)
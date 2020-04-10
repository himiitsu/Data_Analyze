from sympy import *

# ---- ВАШ КОД ТУТ ---


def task_9():
    n = 33
    k = 3
    x = (factorial(n)/(factorial(n-k)*factorial(k)))
    #Тест: 10/x
    return 1/x


# --------------------

proba = task_9()

import unittest


class TestNotebook(unittest.TestCase):
    def test_task(self):
        self.assertAlmostEqual(task_9(), 0.00183, places=5)

unittest.main(argv=[''], verbosity=2, exit=False)
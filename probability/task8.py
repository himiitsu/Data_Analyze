from sympy import *

# ---- ВАШ КОД ТУТ ---


def task_8():
    m = 6
    n = 3
    x = (m*(m-n+2)*(m-n+1))/(m**3)
    return x


# --------------------

proba = task_8()
print(f'p={proba:.2f}')

import unittest


class TestNotebook(unittest.TestCase):
    def test_task(self):
        self.assertAlmostEqual(task_8(), 0.556, places=2)

unittest.main(argv=[''], verbosity=2, exit=False)
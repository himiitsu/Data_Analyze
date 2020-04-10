# ---- ВАШ КОД ТУТ ---

def tp(k,n):
    x = ((k / n) * ((k - 1) / (n - 1)) * ((k - 2) / (n - 2)))
    return x

def task_23():
    n = 20
    return tp(10,n)+tp(8,n)


# --------------------

import unittest


class TestNotebook(unittest.TestCase):
    def test_task(self):
        self.assertAlmostEqual(task_23(), 0.15, places=2)

unittest.main(argv=[''], verbosity=2, exit=False)
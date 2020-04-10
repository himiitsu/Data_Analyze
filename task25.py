# ---- ВАШ КОД ТУТ ---


def task_25():
    x1 = 4/5 * 60 - 1/5 * 15
    x2 = 10/13 * 100 - 3/13 * 30
    x = x1 + x2
    return x


# --------------------



import unittest


class TestNotebook(unittest.TestCase):
    def test_task(self):
        self.assertAlmostEqual(task_25(), 62.46, places=2)

unittest.main(argv=[''], verbosity=2, exit=False)


# ---- ВАШ КОД ТУТ ---


def task_16_1():
    n = 64*63
    m = 64*(64-15)
    return m/n


def task_16_2():
    n = 64*63
    m = 64*14
    return m/n

# --------------------

proba = task_16_1()
print(f'p={proba:.2f}')

proba = task_16_2()
print(f'p={proba:.2f}')

import unittest


class TestNotebook(unittest.TestCase):
    def test_task(self):
        self.assertAlmostEqual(task_16_1(), 0.778, places=3)
        self.assertAlmostEqual(task_16_2(), 0.222, places=3)

unittest.main(argv=[''], verbosity=2, exit=False)
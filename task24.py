# ---- ВАШ КОД ТУТ ---


def task_24():
    p1 = 0.5
    p2 = 0.6
    p3 = 0.7
    return 1-((1-p1)*(1-p2)*(1-p3))


# --------------------


proba = task_24()
print(f'p={proba:.2f}')

import unittest


class TestNotebook(unittest.TestCase):
    def test_task(self):
        self.assertAlmostEqual(task_24(), 0.94, places=2)

unittest.main(argv=[''], verbosity=2, exit=False)
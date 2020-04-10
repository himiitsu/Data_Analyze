

# ---- ВАШ КОД ТУТ ---


def task_13():

    return 3/6*2/5*2/4*1/3*1/2*1


# --------------------

proba = task_13()
print(f'p={proba:.2f}')

import unittest


class TestNotebook(unittest.TestCase):
    def test_task(self):
        self.assertAlmostEqual(task_13(), 0.017, places=3)

unittest.main(argv=[''], verbosity=2, exit=False)
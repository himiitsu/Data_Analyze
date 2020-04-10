# ---- ВАШ КОД ТУТ ---


def task_19(p):
    return (1 - (1-p)**30)


# --------------------

proba = task_19(0.05)
print(f'p={proba:.2f}')

import unittest


class TestNotebook(unittest.TestCase):
    def test_task(self):
        self.assertAlmostEqual(task_19(0.05), 0.78536123, places=6)

unittest.main(argv=[''], verbosity=2, exit=False)
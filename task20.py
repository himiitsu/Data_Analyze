# ---- ВАШ КОД ТУТ ---


def task_20():
    pH1 = 0.1
    pH2 = 0.9
    pAH1 = 0.9
    pAH2 = 0.1
    pA = pH1*pAH1 + pH2*pAH2
    return (pH1*pAH1)/pA


# --------------------

proba = task_20()
print(f'p={proba:.2f}')

import unittest


class TestNotebook(unittest.TestCase):
    def test_task(self):
        self.assertAlmostEqual(task_20(), 0.5, places=2)


unittest.main(argv=[''], verbosity=2, exit=False)
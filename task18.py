# ---- ВАШ КОД ТУТ ---


def task_18():
    pH1 = 0.3
    pH2 = 0.7
    pAH1 = 0.08
    pAH2 = 0.05
    pA = pH1*pAH1 + pH2*pAH2
    return (pH2*pAH2)/pA


# --------------------

proba = task_18()
print(f'p={proba:.2f}')

import unittest


class TestNotebook(unittest.TestCase):
    def test_task(self):
        self.assertAlmostEqual(task_18(), 0.593, places=3)

unittest.main(argv=[''], verbosity=2, exit=False)
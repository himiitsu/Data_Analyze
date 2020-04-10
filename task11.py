from sympy import *

# ---- ВАШ КОД ТУТ ---


def C(k, n):
    ret = factorial(n)/(factorial(n-k)*factorial(k))

    return ret



def task_11():

    #H1 - потеряны 2 чёрных шара
    #H2 - потеряны чёрный и белый шары
    #H3 - потеряны 2 белых шара

    pH1 = 2/21
    pH2 = 10/21
    pH3 = 3/7

    pAH1 = (C(3, 10) / C(3, 13))
    pAH2 = (C(3, 9) / C(3, 13))
    pAH3 = (C(3, 8) / C(3, 13))

    pA = (pH1*pAH1) + (pH2*pAH2) + (pH3*pAH3)

    return (pH1*pAH1)/pA


# --------------------

proba = task_11()
print(f'p={proba:.2f}')



import unittest


class TestNotebook(unittest.TestCase):
    def test_task(self):
        self.assertAlmostEqual(task_11(), 0.152, places=3)

unittest.main(argv=[''], verbosity=2, exit=False)


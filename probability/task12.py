# ---- ВАШ КОД ТУТ ---


def task_12():
    n = 20
    x = ((n-1)/n)
    for i in range(int(n/2)-2):
        x = x * ((n-i-2)/(n-i-1))
    print(x/(n-(i+2)))
    return (x/(n-(i+2)))


# --------------------

proba = task_12()



import unittest


class TestNotebook(unittest.TestCase):
    def test_task(self):
        self.assertAlmostEqual(task_12(), 0.05, places=2)

unittest.main(argv=[''], verbosity=2, exit=False)


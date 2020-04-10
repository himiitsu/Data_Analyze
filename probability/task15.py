

# ---- ВАШ КОД ТУТ ---


def task_15():

    return (11/15*10/14*9/13*8/12)


# --------------------

proba = task_15()
print(f'p={proba:.2f}')



import unittest


class TestNotebook(unittest.TestCase):
    def test_task(self):
        self.assertAlmostEqual(task_15(), 0.242, places=3)

unittest.main(argv=[''], verbosity=2, exit=False)


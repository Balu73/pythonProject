import unittest
def leafYear(x):
    if x%4 == 0:
        if x%100 == 0:
            if x%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

class MyTestCase(unittest.TestCase):
    def test_leafYear(self):
        self.assertEqual(leafYear(1600),True)  # add assertion here
        self.assertEqual(leafYear(1620),True)  # add assertion here
        self.assertEqual(leafYear(1621),False)  # add assertion here
        self.assertEqual(leafYear(1616),True)  # add assertion here
        self.assertEqual(leafYear(1663),False)  # add assertion here






if __name__ == '__main__':
    unittest.main()

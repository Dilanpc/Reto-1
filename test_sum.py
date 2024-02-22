import unittest
from sumaDeConsecutivos import mayor_suma

class TestMaxConsecutiveSum(unittest.TestCase):
  def test_mayor_suma(self):
    self.assertEqual(mayor_suma([1, 2, 3, 4, 5]), 9)
    self.assertEqual(mayor_suma([5, 2, 8, 1, 3]), 10)
    self.assertEqual(mayor_suma([-1, -2, -3, -4, -5]), -3)
    self.assertEqual(mayor_suma([2, 3, -5, 8, -1]), 7)
    self.assertEqual(mayor_suma([2, 3, 5, 8, 1]), 13)

if __name__ == '__main__':
    unittest.main()
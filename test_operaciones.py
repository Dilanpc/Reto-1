import unittest
from Operaciones import operar

class TestBasicOperation(unittest.TestCase):
  def setUp(self) -> None:
    print("Starting test")
  
  def tearDown(self) -> None:
    pass

  def test_addition(self):
    self.assertEqual(operar(2, 3, "+"), 5)

  def test_subtraction(self):
    self.assertEqual(operar(2, 3, "-"), -1)

  def test_multiplication(self):
    self.assertEqual(operar(2, 3, "*"), 6)

  def test_division(self):
    self.assertEqual(operar(6, 3, "/"), 2)


if __name__ == "__main__":
  unittest.main()

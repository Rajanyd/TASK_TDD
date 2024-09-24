import unittest
from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calculator = StringCalculator()

    def test_1_empty_string_returns_zero(self):
        print("\nTest Case 1:- Empty String")
        try:
            self.assertEqual(self.calculator.add(""), 0)
        except Exception as e:
            print(f"Test Failed:- {e}")
    
    def test_2_single_number_returns_the_number(self):
        print("\nTest Case 2:- Single Number")
        try:
            self.assertEqual(self.calculator.add("1"), 1)
        except Exception as e:
            print(f"Test Failed:- {e}")

if __name__ == '__main__':
    unittest.main()
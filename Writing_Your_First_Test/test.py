import unittest
from fractions import Fraction
from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
    
""""
These tests validate the logic in the methods created.  When running the tests you create an expected result 
from the alogorithm provided.  As the tests run, solutions are valdidated by comparing the acutal results to 
the expected result.  If a test passes, it vaguely acknowledges the method.  However if a test fails. The algorithm 
assertion is shown with the method that failed.

For the above example, when run, the first method passed and second method failed providing the following comment 
to the console:
"""

"""
======================================================================
FAIL: test_list_fraction (__main__.TestSum.test_list_fraction)
Test that it can sum a list of fractions
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\Users\Mike\OneDrive\Documents\Ivy Tech\SDEV220\Module 5\M05_ProgrammingAssignment_MGentile\Writing_Your_First_Test\test.py", line 21, in test_list_fraction
    self.assertEqual(result, 1)
AssertionError: Fraction(9, 10) != 1

----------------------------------------------------------------------
Ran 2 tests in 0.003s

FAILED (failures=1)        
"""
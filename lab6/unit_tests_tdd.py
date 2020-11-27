import unittest
from lab6.some_functions import linear_or_square_equation, equation_of_a_straight_line


class TestSomeFunctions(unittest.TestCase):
    def test_linear_or_square_equation(self):
        self.assertEqual(linear_or_square_equation(2, 4, 2), -1)
        self.assertEqual(linear_or_square_equation(1, 0, 2), None)
        self.assertEqual(set(linear_or_square_equation(-1.4, -5.4, 2.3)), {-4.244223582492476, 0.38708072534961846})
        self.assertEqual(set(linear_or_square_equation(-30.5, -5.4, 2.3)), {-0.3770491803278688, 0.2})
        self.assertEqual(linear_or_square_equation(0, 3, 20), -20/3)
        self.assertEqual(linear_or_square_equation(0, 0, 2.433), None)
        self.assertEqual(linear_or_square_equation(0, 0, 0), "Infinitely many solutions")
        self.assertEqual(linear_or_square_equation(0, 0, -100.3), None)
        self.assertRaises(ValueError, lambda: linear_or_square_equation("string", 2, "string2"))

    def test_equation_of_straight_line(self):
        self.assertEqual(equation_of_a_straight_line(5, 6, 7, 11), "y=2.5x-6.5")
        self.assertEqual(equation_of_a_straight_line(-10, -23, -4, 10), "y=5.5x+32.0")
        self.assertEqual(equation_of_a_straight_line(6.5, -2.3, -2.3, 4.33424), "y=-0.7538909090909091x+2.6002909090909094")
        self.assertEqual(equation_of_a_straight_line(2, -3, 2, -3), "Many equations of a straight line")
        self.assertEqual(equation_of_a_straight_line(0, 0, 0, 0), "Many equations of a straight line")
        self.assertEqual(equation_of_a_straight_line(-10.3, 255, -10.3, -567.2), "x=-10.3")
        self.assertEqual(equation_of_a_straight_line(-3, -4.5, 300, -4.5), "y=-4.5")
        self.assertRaises(ValueError, lambda: equation_of_a_straight_line("string", 2, "string2", "string3"))

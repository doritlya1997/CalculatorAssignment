import unittest

from calculator import Calculator


class MyTestCase(unittest.TestCase):

    def test_no_assignments_return_empty(self):
        expressions = []
        cal = Calculator(expressions)
        result = cal.evaluate()
        self.assertEqual(result, {})

    def test_no_assignment_return_empty(self):
        expressions = ["2 + 3"]
        cal = Calculator(expressions)
        result = cal.evaluate()
        self.assertEqual(result, {})

    def test_assignment_into_num_return_empty(self):
        expressions = ["1 = 2 + 3"]
        cal = Calculator(expressions)
        result = cal.evaluate()
        self.assertEqual(result, {})

    # Single assignment

    def test_assignment_of_num_returns_num(self):
        expressions = ["i = 2"]
        cal = Calculator(expressions)
        result = cal.evaluate()
        self.assertEqual({"i": 2}, result)

    def test_assignment_of_addition_of_two_numbers_returns_sum(self):
        expressions = ["i = 2 + 3"]
        cal = Calculator(expressions)
        result = cal.evaluate()
        self.assertEqual({"i": 5}, result)

    def test_assignment_of_substraction_of_two_numbers_returns_diff(self):
        expressions = ["i = 3 - 2"]
        cal = Calculator(expressions)
        result = cal.evaluate()
        self.assertEqual({"i": 1}, result)

    def test_assignment_of_multiplication_of_two_numbers_returns_multi(self):
        expressions = ["i = 3 * 2"]
        cal = Calculator(expressions)
        result = cal.evaluate()
        self.assertEqual({"i": 6}, result)

    def test_assignment_of_division_of_two_numbers_returns_division(self):
        expressions = ["i = 4 / 2"]
        cal = Calculator(expressions)
        result = cal.evaluate()
        self.assertEqual({"i": 2}, result)

    def test_assignment_of_division_by_zero_returns_empty(self):
        expressions = ["i = 4 / 0"]
        cal = Calculator(expressions)
        result = cal.evaluate()
        self.assertEqual({}, result)

    def test_assignment_with_parenthesis(self):
        expressions = ["i = 40 - ( 4 + 6 / 2 ) * 5"]
        cal = Calculator(expressions)
        result = cal.evaluate()
        self.assertEqual({"i": 5}, result)

    # Multiple assignments

    def test_addition_assignment_of_two_number_returns_sum(self):
        expressions = ["i = 2", "i += 3"]
        cal = Calculator(expressions)
        result = cal.evaluate()
        self.assertEqual({"i": 5}, result)

    def test_substraction_assignment_of_two_numbers_returns_diff(self):
        expressions = ["i = 3", "i -= 2"]
        cal = Calculator(expressions)
        result = cal.evaluate()
        self.assertEqual({"i": 1}, result)

    def test_multiplication_assignment_of_two_numbers_returns_multi(self):
        expressions = ["i = 3", "i *= 2"]
        cal = Calculator(expressions)
        result = cal.evaluate()
        self.assertEqual({"i": 6}, result)

    def test_division_assignment_of_division_of_two_numbers_returns_division(self):
        expressions = ["i = 4", "i /= 2"]
        cal = Calculator(expressions)
        result = cal.evaluate()
        self.assertEqual({"i": 2}, result)

    def test_division_assignment_of_zero_returns_empty(self):
        expressions = ["i = 4", "i /= 0"]
        cal = Calculator(expressions)
        result = cal.evaluate()
        self.assertEqual({}, result)

    # assignment without previous_value

    def test_addition_assignment_without_previous_value_returns_empty(self):
        expressions = ["i += 3"]
        cal = Calculator(expressions)
        result = cal.evaluate()
        self.assertEqual({}, result)

    def test_substraction_assignment_without_previous_value_returns_empty(self):
        expressions = ["i -= 2"]
        cal = Calculator(expressions)
        result = cal.evaluate()
        self.assertEqual({}, result)

    def test_multiplication_assignment_without_previous_value_returns_empty(self):
        expressions = ["i *= 2"]
        cal = Calculator(expressions)
        result = cal.evaluate()
        self.assertEqual({}, result)

    def test_division_assignment_without_previous_value_returns_empty(self):
        expressions = ["i /= 2"]
        cal = Calculator(expressions)
        result = cal.evaluate()
        self.assertEqual({}, result)

    # Multiple assignments based on variables

    def test_assignment_of_var_returns_var(self):
        expressions = ["a = 2", "b = a"]
        cal = Calculator(expressions)
        result = cal.evaluate()
        self.assertEqual({"a": 2, "b": 2}, result)

    def test_assignment_of_addition_of_var_and_num_returns_sum(self):
        expressions = ["a = 2", "b = a + 3"]
        cal = Calculator(expressions)
        result = cal.evaluate()
        self.assertEqual({"a": 2, "b": 5}, result)

    def test_assignment_of_substraction_of_var_and_num_returns_sum(self):
        expressions = ["a = 3", "b = a - 2"]
        cal = Calculator(expressions)
        result = cal.evaluate()
        self.assertEqual({"a": 3, "b": 1}, result)

    def test_assignment_of_multiplication_of_var_and_num_returns_sum(self):
        expressions = ["a = 3", "b = 2 * a"]
        cal = Calculator(expressions)
        result = cal.evaluate()
        self.assertEqual({"a": 3, "b": 6}, result)

    def test_assignment_of_division_of_var_and_num_returns_sum(self):
        expressions = ["a = 8", "b = a / 4"]
        cal = Calculator(expressions)
        result = cal.evaluate()
        self.assertEqual({"a": 8, "b": 2}, result)

    # Multiple assignments based on incrementing/decrementing variables

    def test_assignment_of_postfix_incrementing_var(self):
        expressions = ["a = 2", "b = a++"]
        cal = Calculator(expressions)
        result = cal.evaluate()
        self.assertEqual({"a": 3, "b": 2}, result)

    def test_assignment_of_prefix_incrementing_var(self):
        expressions = ["a = 2", "b = ++a"]
        cal = Calculator(expressions)
        result = cal.evaluate()
        self.assertEqual({"a": 3, "b": 3}, result)

    def test_assignment_of_postfix_decrementing_var(self):
        expressions = ["a = 2", "b = a--"]
        cal = Calculator(expressions)
        result = cal.evaluate()
        self.assertEqual({"a": 1, "b": 2}, result)

    def test_assignment_of_prefix_decrementing_var(self):
        expressions = ["a = 2", "b = --a"]
        cal = Calculator(expressions)
        result = cal.evaluate()
        self.assertEqual({"a": 1, "b": 1}, result)

if __name__ == '__main__':
    unittest.main()

import unittest
from math_quiz import generate_num, generate_operator, perform_operation


class TestMathGame(unittest.TestCase):

    def test_generate_num(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_num(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val,
                            f"{rand_num} is not within the range {min_val} to {max_val}")

    def test_generate_operator(self):
         """ Checks if the operators are being generated properly"""
         operator_list = ["*", "+", "-"]
         for _ in range(1000):
              operator = generate_operator()
              self.assertIn(operator, operator_list, f"{operator} not valid!")

    def test_perform_operation(self):
            """ Checks if the operation and problems are being generated correctly."""
            test_cases = [
                (5, 2, '+', '5 + 2', 7),  
                (10, 4, '*', '10 * 4', 40), 
                (5, 2, '-', '5 - 2', 3),
                (2, 4, '-', '2 - 4', -2)    
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                 prob, ans = perform_operation(num1, num2, operator)
                 self.assertEqual(prob, expected_problem, f"Incorrect problem format!")
                 self.assertEqual(ans, expected_answer, f"Answer is incorrect!")

if __name__ == "__main__":
    unittest.main()

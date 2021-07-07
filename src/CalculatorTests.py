import unittest
from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    # Unit Test for Addition
    def test_add_method_calculator(self):
        test_data = CsvReader("/src/datafile/Addition.csv").get_data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    # Unit Test for Subtraction
    def test_subtraction_method_calculator(self):
        test_data = CsvReader('/src/datafile/Subtraction.csv').data
        for row in test_data:
            self.assertNotEqual(self.calculator.subtract(row['Value 3'], row['Value 4']), int(row['Result']))
            self.assertNotEqual(self.calculator.result, int(row['Result']))

    # Unit Test for Multiplication
    def test_multiply_method_calculator(self):
        test_data = CsvReader("/src/datafile/Multiplication.csv").get_data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 5'], row['Value 6']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    # Unit Test for Division
    def test_divide_method_calculator(self):
        test_data = CsvReader("/src/datafile/Division.csv").get_data
        for row in test_data:
            self.assertAlmostEqual(self.calculator.divide(row['Value 8'], row['Value 7']), float(row['Result']))
            self.assertAlmostEqual(self.calculator.result, float(row['Result']))

    # Unit Test for Square
    def test_square_method_calculator(self):
        test_data = CsvReader("/src/datafile/Square.csv").get_data
        for row in test_data:
            self.assertAlmostEqual(self.calculator.square(row['Value 9']), float(row['Result']))
            self.assertAlmostEqual(self.calculator.result, float(row['Result']))

    # Unit Test for Squareroot
    def test_squareroot_method_calculator(self):
        test_data = CsvReader("/src/datafile/Square Root.csv").get_data
        for row in test_data:
            self.assertAlmostEqual(self.calculator.square_root(row['Value 10']), float(row['Result']))
            self.assertAlmostEqual(self.calculator.result, float(row['Result']))

if __name__ == "__main__":
    unittest.main()

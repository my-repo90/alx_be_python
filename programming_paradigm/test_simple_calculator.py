import unittest 
from simple_calculator import SimpleCalculator 

class test_calculations(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(12 , 1) , 13)

    def test_substraction(self):
        self.assertEqual(self.calc.subtract(1 , 12) , -11)
        self.assertEqual(self.calc.subtract(12 , 12) , 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(1 , 10) , 10)

    def test_divide(self):
        self.assertEqual(self.calc.divide(2 , 1) , 2)

        #self.assertRaises(ZeroDivisionError , self.calc.divide , 10 , 0)
        self.assertEqual(self.calc.divide(10 , 0) , None)
if __name__ == '__main__':
    unittest.main()
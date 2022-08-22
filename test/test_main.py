import unittest
from code import main

class TestAlgNum(unittest.TestCase): 
    def test_init(self):
        a=main.AlgNum({1:main.Fraction(6),2:main.Fraction(5)})
        self.assertEqual(a.data,{1:main.Fraction(6),2:main.Fraction(5)})
    def test_strandrepr(self):
        a=main.AlgNum({1:main.Fraction(6),2:main.Fraction(5)})
        self.assertEqual(str(a),"AlgNum[1: Fraction(6, 1), 2: Fraction(5, 1)]")
        self.assertEqual(repr(a),"AlgNum({1: Fraction(6, 1), 2: Fraction(5, 1)})")
    def test_add(self):
        a=main.AlgNum({1:main.Fraction(6),2:main.Fraction(5)})
        b=main.AlgNum({2:main.Fraction(6),3:main.Fraction(5)})
        c=a+b
        self.assertEqual(c.data,{1:main.Fraction(6),2:main.Fraction(11),3:main.Fraction(5)})

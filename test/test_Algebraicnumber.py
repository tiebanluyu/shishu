import unittest
from code import Algebraicnumber

class testAlgebraicnumber:
    def test_init(self):
        a=Algebraicnumber.Surd({1:5,2:7})
        self.assertEqual(a.data,{2:7})
        self.assertEqual(a.confficient,5)
    def test_mul(self):
        a=Algebraicnumber.Surd({1:5,2:7})
        b=a*a
        self.assertEqual(b.data,{})
        self.assertEqual(a.confficient,175)
import unittest
from code import Algebraicnumber

class testAlgebraicnumber:
    def test_init(self):
        a=Algebraicnumber.Surd({1:5,2:7})
        self.assertEqual(a.data,{2:7})
        self.assertEqual(a.confficient,5)
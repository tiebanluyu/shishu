import unittest
from code import Algebraicnumber
Surd=Algebraicnumber.Surd
Polymerization=Algebraicnumber.Polymerization
class testSurd(unittest.TestCase):
    def test_init(self):
        a=Surd({1:5,2:7})
        self.assertEqual(a.data,{2:7})
        self.assertEqual(a.confficient,5)
    def test_mul(self):
        a=Surd({3:7})
        b=a*a*a
        self.assertEqual(a.data,{})
        self.assertEqual(a.confficient,7)
    def test_repr(self):
        a=surd({3:4,2:6})
        self.assertEqual(repr(a),"({3: 4, 2: 6}, 1)")
         
class testPolymerization(unittest.TestCase):
    def test_init(self):
        a=Surd({1:3})
        a=Polymerization({a:123})
    def test_add(self):
        """
        a=Surd({2:7})
        b=a*a
        c=Polymerization(a,b)
        self.assertEqual((c+c).data,{{2: 7}: 2, {}: 14})"""
        

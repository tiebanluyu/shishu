import unittest
from code import Algebraicnumber
Surd=Algebraicnumber.Surd
class testSurd:
    def test_init(self):
        a=Surd({1:5,2:7})
        self.assertEqual(a.data,{2:7})
        self.assertEqual(a.confficient,5)
    def test_mul(self):
        a=Surd({3:7,4:3})
        b=a*a*a
        self.assertEqual(a.data,{})
        import math
        self.assertEqual(a.confficient,7)    
class testPolymerization:
    def test_init(self):
        pass
    def test_add(self):
        a=Surd({2:7})
        b=a*a
        c=Polymerization(a,b)
        self.assertEqual((c+c).data,({{2: 7}: 2, {}: 14},))
        

import unittest
from code import Algebraicnumber
Surd=Algebraicnumber.Surd
Polymerization=Algebraicnumber.Polymerization
frozendict=Algebraicnumber.frozendict
class testSurd(unittest.TestCase):
    def test_init(self):
        a=Surd({1:5,2:7})
        self.assertEqual(a.data,{2:7})
        self.assertEqual(a.confficient,5)
    def test_mul(self):
        a=Surd({3:7})
        b=a*a*a
        self.assertEqual(b.data,{})
        self.assertEqual(b.confficient,7)
    def test_repr(self):
        a=Surd({3:4,2:6})
        self.assertEqual(repr(a),"({3: 4, 2: 6}, 1)")
         
class testPolymerization(unittest.TestCase):
    def test_init(self):
        a=Surd({1:3})
        a=Polymerization({a:123})
    def test_add(self):
        
        a=Surd({2:7})
        b=a*a
        c=Polymerization(a,b)
        self.assertEqual((c+c).data,{frozendict({2: 7}): 2, frozendict({}): 14})
    def test_sub(self):
        
        a=Surd({2:7})
        b=Surd({5:4})
        c=Polymerization(a,b)
        self.assertEqual(c.data,{frozendict({2: 7}): 1, frozendict({5:4}): 1})
    def test_mul(self):
        a=Polymerization({Surd({2:7}):3,Surd({2:5}):1})
        b=Polymerization({Surd({2:7}):4,Surd({2:6}):2})
        c=b*a
        

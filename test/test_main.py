import unittest
from code import main

class TestAlgNum(unittest.TestCase): 
    def test_init(self):
        a=main.AlgNum({1:6,2:5})
        self.assertEqual(a.data,{1:6,2:5})
    def test_strandrepr(self):
        a=main.AlgNum({1:6,2:5})
        self.assertEqual(str(a),"AlgNum[1: 6, 2: 5]")
        self.assertEqual(repr(a),"AlgNum({1: 6, 2: 5})")
    def test_add(self):
        a=main.AlgNum({1:6,2:5})
        b=main.AlgNum({2:6,3:5})
        c=a+b
        self.assertEqual(c.data,{1:6,2:11,3:5})
    
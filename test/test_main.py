import unittest
from code import main

class TestAlgNum(unittest.TestCase): 
    def test_init(self):
        a=main.AlgNum({1:6,2:5})
        self.assertEqual(a.data,{1:6,2:5})
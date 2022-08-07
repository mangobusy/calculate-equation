import unittest
from Assessment2 import assessment2

class uni_test(unittest.TestCase):
    def test1(self):
        self.assertFalse(assessment2.print_exampleTree(['(','(','3','+','2',')','*','5',')']),False)
    def test2(self):
        self.assertFalse(assessment2.is_matched(['(','(','3','+','2',')','*','5',')']))
    def test3(self):
        self.assertFalse(assessment2.is_valid(['(','(','3','+','2',')','*','5',')']))



if __name__=='__main__':
    unittest.main()
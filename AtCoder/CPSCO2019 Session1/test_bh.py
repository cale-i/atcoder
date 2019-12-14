import unittest
import bh

class BH(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual('Yes', bh.bh('ababcc'))

    def test_2(self):
        self.assertEqual('Yes', bh.bh('reiwa'))

    def test_3(self):
        self.assertEqual('No', bh.bh('cpsco'))

    def test_4(self):
        self.assertEqual('No', bh.bh('aaaabaaa'))

    def test_5(self):
        self.assertEqual('No',bh.bh(input()))

if __name__ == "__main__":
    unittest.main()
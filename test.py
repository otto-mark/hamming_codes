import unittest

from hamming import *

class HammingTest(unittest.TestCase):
    
    def test_hammingSEC_7_4(self):
        self.assertEqual(makeHammingCodeSEC("1001"), "1001100")
        self.assertEqual(makeHammingCodeSEC("1000"), "1001011")
        self.assertEqual(makeHammingCodeSEC("0000"), "0000000")
        self.assertEqual(makeHammingCodeSEC("1111"), "1111111")
        self.assertEqual(makeHammingCodeSEC("1100"), "1100001")
        
    def test_hammingSECDEC_8_4(self):
        self.assertEqual(makeHammingCodeSECDED("1001"), "10011001")
        self.assertEqual(makeHammingCodeSECDED("1000"), "10010110")
        self.assertEqual(makeHammingCodeSECDED("0000"), "00000000")
        self.assertEqual(makeHammingCodeSECDED("1111"), "11111111")
        self.assertEqual(makeHammingCodeSECDED("1100"), "11000011")
        
if __name__ == '__main__':
    unittest.main()
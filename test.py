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
        
    def test_hammingSEC_decode(self):
        self.assertEqual(decodeHammingSEC(1001100), ("1001", False))
        self.assertEqual(decodeHammingSEC(1001101), ("1001", True))
        self.assertEqual(decodeHammingSEC(1001011), ("1000", False))
        self.assertEqual(decodeHammingSEC(1101011), ("1000", True))
        self.assertEqual(decodeHammingSEC(1100011), ("1100", True))
        self.assertEqual(decodeHammingSEC("0001011"), ("1000", True))
    
    def test_hammingSECDED_decode(self):
        self.assertEqual(decodeHammingSECDED("10010110"), ("1000", NO_FLIP))
        self.assertEqual(decodeHammingSECDED("10010100"), ("1000", SEC_FLIP))
        self.assertEqual(decodeHammingSECDED("10010101"), ("1000", DED_FLIP))
        self.assertEqual(decodeHammingSECDED("10111110"), ("1111", DED_FLIP))
        
        
        
    def test_berger_encoding(self):
        self.assertEqual(makeBergerCode("10001"), "10001"+"101")
        self.assertEqual(makeBergerCode("000"), "000"+"11")
        self.assertEqual(makeBergerCode("1111111"), "1111111"+"000")
        self.assertEqual(makeBergerCode("11111111"), "11111111"+"0111")
        self.assertEqual(makeBergerCode("1010111010010101"), "1010111010010101"+"10110")
        
    def test_berger_decoding(self):
        self.assertEqual(decodeBerger("10001"+"101"), ("10001", True))
        self.assertEqual(decodeBerger("000"+"11"), ("000", True))
        self.assertEqual(decodeBerger("1111111"+"000"), ("1111111", True))
        self.assertEqual(decodeBerger("11111111"+"0111"), ("11111111", True))
        self.assertEqual(decodeBerger("1010111010010101"+"10110"), ("1010111010010101", True))
        
        self.assertEqual(decodeBerger("1010111010010101"+"11110"), ("1010111010010101", False))
        self.assertEqual(decodeBerger("111111111"+"0111"), ("111111111", False))
        self.assertEqual(decodeBerger("1111101"+"000"), ("1111101", False))
        self.assertEqual(decodeBerger("111"+"11"), ("111", False))
        self.assertEqual(decodeBerger("1010001"+"000"), ("1010001", False))
        self.assertEqual(decodeBerger("11101"+"101"), ("11101", False))
        
        
        
if __name__ == '__main__':
    unittest.main()
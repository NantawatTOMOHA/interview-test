import unittest
def Int_Roman(num):
    I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    M = ["", "M", "MM", "MMM"]

    return M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[num % 10]

class TestNumber(unittest.TestCase):
    def test_Int_Roman_1(self):
        test = Int_Roman(3)
        result = "III" 
        self.assertEqual(result,test)
    def test_Int_Roman_2(self):
        test = Int_Roman(58)
        result = "LVIII"
        self.assertEqual(result,test)
    def test_Int_Roman_3(self):
        test = Int_Roman(1994)
        result = "MCMXCIV"
        self.assertEqual(result,test)

if __name__ == '__main__':
       unittest.main()
      
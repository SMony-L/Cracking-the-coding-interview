# Given two strings, write a method to decide if one is a permuation of others
import unittest
from collections import Counter
class Solution():
    # Brute force
    # O(N)
    # def checkPerm(self, str1, str2):
    #   if (len(str1) != len(str2)): return False
        
        # sort the two strings
        # sortedString1 = sorted(str1)
        # sortedString2 = sorted(str2)

        # check if strings are equal
        # for i in range(len(sortedString1)):
        #     if (sortedString1[i] == sortedString2[i]):
        #         return True
        # return False

        # one-line check if strings are equal
        # return (sorted(str1)).__eq__(sorted(str2))

    # 2nd methods using collections Counter
    # O(N)
    # def checkPerm(self, str1, str2):
    #     if (len(str1) != len(str2)) : return False
    #     countStr1 = Counter(str1)
    #     countStr2 = Counter(str2)
    #     if (countStr1 == countStr2):
    #         return True
    #     return False

    # 3rd methods
    # using all function to check whether all element in str1 is in str2
    # O(N^2)
    def checkPerm(self, str1, str2):
        if (len(str1) != len(str2)): return False
        else: return all(i in str2 for i in str1)

class Test(unittest.TestCase):
    
    string1 = [
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    ]
    string2 = [
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    ]

    def testCheckPerm(self):
        # True check
        for firstString, secondString in self.string1:
            result = Solution()
            actual = result.checkPerm(firstString,secondString)
            self.assertTrue(actual)
        
        # False check
        for firstString, secondString in self.string2:
            result = Solution()
            actual = result.checkPerm(firstString,secondString)
            self.assertFalse(actual)
        

if __name__ == "__main__":
    unittest.main()
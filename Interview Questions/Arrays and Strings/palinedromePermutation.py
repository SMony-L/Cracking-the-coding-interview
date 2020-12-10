# Given a string, write a function to check if it is a permutation of a palindrome. 
# A palindrome is a word or phrase that is the same forwards and backwards. 
# A permutation is a a rearrangement of letters. The palindrome does not need to be limited to just a dictionary words.
import unittest
from itertools import permutations

class Solution():
    
    def checkPalinPermut(self, str1):
        perm = permutations(str1.replace(' ', '').lower())
        result = [i for i in set(perm)]
        actual = [''.join(tup) for tup in result]
        for i in actual:
            rev = ''.join(reversed(i))
            if i == rev:
                return True
         
        return False
        

class Test(unittest.TestCase):

    str1 = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]
    # str1 = [('ABAB', True), ('aabbcadad', True)]
    def testPalinDromePermutation(self):
        for [testString, expected] in self.str1:
            result = Solution()
            actual = result.checkPalinPermut(testString)
            self.assertEqual(actual, expected)
        

if __name__ == '__main__':
    unittest.main()
# Write a method to replace all spaces in a string with '%20'. 
# You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.
# (Note: if implementing in Java, please use a character array so that you can perform this operation in place.)
import unittest
class Solution():
    
    # 1st Approach
    # Using replace built-in function
    # O(1)
    # def urlify(self,str1,length):
    #     result = ''.join(str1).strip()
    #     return list(result.replace(' ', '%20'))
        
    # 2nd approach
    # Using join() and split()
    # O(1)
    def urlify(self, str1, length):
        result = ''.join(str1).strip()
        return (list('%20'.join(result.split())))

    # 3rd approach
    # Using List comphrehension
    # O(N)
    # def urlify(self,str1,length):
    #     result = ''.join(str1).strip()
    #     temp = ''
    #     for i in result:
    #         temp += '%20' if i == ' ' else i
    #     return list(temp)
        
class Test(unittest.TestCase):
    str1 = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]
    
    # isEqual
    def testUrlify(self):
        for [testString, length, expected] in self.str1:
            result = Solution()
            actual = result.urlify(testString, length)
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()

# Implement an algorithm determine if a string has all unique characters. 
# What if you cannot use additional data structure

import unittest
from collections import Counter

# Brute Force
# O(N^2)
# def uniqueChar(string):
#     for i in range(len(string)):
#         for j in range(i+1,len(string)):
#             if(string[i] == string[j]):
#                 return False
#     return True

# 2nd methods
# Using Counter
# O(N)
def uniqueChar(string):
    newString = Counter(string)
    for i, j in newString.items():
        if j > 1:
            return False
    return True

# 3rd methods
# Using dictionary to store char
# O(N)
# def uniqueChar(string):
#     myDict = {}
#     for i in range(len(string)):
#         # if the value already in dict
#         if string[i] in myDict:
#             return False
#         # if not add the value to dict
#         else:
#             myDict[string[i]] = i
#     return True

# 4th methods
# Using set of ascii characters
# def uniqueChar(string):
#     if len(string) > 128:
#         return False
    
#     charSet = [False for _ in range(128)]
#     for char in string:
#         val = ord(char)
#         if charSet[val]:
#             return False
#         charSet[val] = True
#     return True
class Test(unittest.TestCase):
    
    string1 = [('abced10'), ('qweasdzxc'), ('')]
    string2 = [('HelloWorld'), ('Programming'), ('()()')]
    def test_unique(self):
        # true check
        for testString in self.string1:
            result = uniqueChar(testString)
            self.assertTrue(result)

        for testString in self.string2:
            result = uniqueChar(testString)
            self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()

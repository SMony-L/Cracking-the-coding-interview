import unittest
from collections import Counter
class Solution():
    def checkOneAway(self,str1, str2):
        # if absolute value of len(s1) - len(s2) > 1 return False
        if (abs(len(str1) - len(str2)) > 1): return False
        
        shortString = str1 if len(str1) < len(str2) else str2
        longString = str2 if len(str1) < len(str2) else str1
    
        i = 0
        j = 0
        counter = 0
        while (i < len(shortString)):
            if longString[j] != shortString[i]:
                counter += 1
                if counter > 1:
                    return False
                if len(shortString) == len(longString):
                    i+=1
            else:
                i+=1
            j+=1
        return True
        # if one is empty or both is empty return False
        # if len equal then it is replaced
        if len(str1) == len(str2):
            return oneReplace(str1,str2)
        # if len is 1 greater then something has been inserted
        elif len(str1) + 1 == len(str2):
            return oneInsert(str1,str2)
        # if len is 1 smaller then something has been removed
        elif len(str1) - 1 == len(str2):
            return oneRemove(str1, str2)
    def oneReplace(self, str1, str2):
        pass
        # Todo
    def oneInsert(self,str1, str2):
        pass
        # Todo
    def oneRemove(self,str1, str2):
        # Todo
        pass

class Test(unittest.TestCase):
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = Solution().checkOneAway(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
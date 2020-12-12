import unittest

class Solution():
    def checkStringComp(self, str1):
        
        counter = 1
        newList = []
        for i in range(1,len(str1)):
            if (str1[i] != str1[i-1]):
                newList.append(str1[i-1]+ str(counter))
                counter = 0 
            counter+=1
        newList.append(str1[i-1] + str(counter))      
        return str1 if len(''.join(newList)) > len(str1) else ''.join(newList)

class Test(unittest.TestCase):
    data = [
        ('aabcccccaaa','a2b1c5a3'), 
        ('abcde','abcde'), 
        ('aaaaabbbbbcccccdddddaaa','a5b5c5d5a3')]

    def testCheckStringComp(self):
        for [realString, expected] in self.data:
            actual = Solution().checkStringComp(realString)
            self.assertEqual(actual, expected)
    
    
if __name__ == '__main__':
    unittest.main()



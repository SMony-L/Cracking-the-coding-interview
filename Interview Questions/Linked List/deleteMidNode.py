class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None
    
    def insertNode(self, data):
        newNode = ListNode(data)
        newNode.next = self.head
        self.head = newNode

    # 1st solution with access to head node
    # O(n) time and O(1) space
    # def deleteMidNode(self, ll):
    #     temp = curr = ll.head
    #     length = 0
    #     while (temp):
    #         temp = temp.next
    #         length += 1
        
    #     for i in range((length // 2)-1):
    #         curr = curr.next

    #     curr.next = curr.next.next

    #     return ll
    

    # 2nd solution without access to head node but only the actual node that will be deleted
    def deleteMidNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

    def printLinkedList(self):
        curr = self.head
        while (curr):
            print(curr.val)
            curr = curr.next
firstList = Solution()
firstList.insertNode('a')
firstList.insertNode('b')
firstList.insertNode('c')
midNode = firstList.head
firstList.insertNode('d')
firstList.insertNode('e')
firstList.insertNode('f')
firstList.printLinkedList()
print("--")
firstList.deleteMidNode(midNode)
firstList.printLinkedList()
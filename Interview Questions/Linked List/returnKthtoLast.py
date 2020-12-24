class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None
    
    def insertNode(self, data):
        newNode = ListNode(data)
        newNode.next = self.head
        self.head = newNode

    # Optimal Solution
    # O(n) time and O(1) space
    # def findKthtoLast(self, ll, k):
    #     p1 = ll.head
    #     p2 = ll.head
        
    #     for i in range(k):
    #         if p1 is None: return None
    #         p1 = p1.next

    #     while (p1):
    #         p1 = p1.next
    #         p2 = p2.next
    #     return p2.val

    # 2nd solution
    # Get the length then length - k
    def findKthtoLast(self, ll, k):
        temp = prev = ll.head

        length = 0
        while temp:
            temp = temp.next
            length += 1
        
        for i in range(length - k):
            prev = prev.next
        return prev.val

    def printLinkedList(self):
        curr = self.head
        while (curr):
            print(curr.val)
            curr = curr.next

firstList = Solution()
firstList.insertNode(5)
firstList.insertNode(7)
firstList.insertNode(99)
firstList.insertNode(8)
firstList.printLinkedList()

print('Kth to the last element val is = {}'.format(firstList.findKthtoLast(firstList,2)))

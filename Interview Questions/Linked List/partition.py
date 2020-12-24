class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.head = None

    def insertNode(self,data):
        newNode = ListNode(data)
        newNode.next = self.head
        self.head = newNode

    def printLinkedList(self):
        curr = self.head
        while (curr):
            print(curr.val)
            curr = curr.next

    def partition(self,ll, x):
        
        # if temp val is < x add to smallList
        # if temp val is >= x add to bigList
        current = ll.tail = ll.head
        while current:
            nextNode = current.next
            current.next = None
            if current.val < x:
                current.next = ll.head
                ll.head = current
            else:
                ll.tail.next = current
                ll.tail = current
            current = nextNode
        
        # Error check in case all nodes are less than x
        if ll.tail.next is not None:
            ll.tail.next = None

myList = Solution()
listDat = [1,2,10,5,8,5,3]
for i in listDat:
    myList.insertNode(i)
myList.printLinkedList()
print('--')
myList.partition(myList,5)
myList.printLinkedList()
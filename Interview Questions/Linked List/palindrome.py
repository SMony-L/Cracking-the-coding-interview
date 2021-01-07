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
        while curr:
            print(curr.val)
            curr = curr.next

    # 1st method
    # Reverse the LinkedList and Compare

    def isPalindrome(self, ll):

        reverseList = ListNode()
        reverseList = self.reverseAndClone(ll)
        
        return self.isEqual(ll,reverseList)

    def reverseAndClone(self,ll):
        self.head = None
        while ll:
            n = ListNode(ll.val) # copy val
            
            # reverse pointer
            n.next = self.head
            self.head = n
            ll = ll.next

        return self.head

    def isEqual(self,l1, l2):
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        
        return l1 is None and l2 is None


    # 2nd method
    # Two Pointers and stack

    # def isPalindrome(self, ll):
    #     fast = slow = self.head

    #     stack = []

    #     while fast and fast.next:
    #         stack.append(slow.val)
    #         slow = slow.next
    #         fast = fast.next.next
  
    #     if fast is not None:
    #         slow = slow.next

    #     while slow:
    #         top = stack.pop()
    #         if top != slow.val:
    #             return False
    #         slow = slow.next

    #     return True
    
    

myLL = Solution()

myLL.insertNode(0)
myLL.insertNode(1)
myLL.insertNode(2)
myLL.insertNode(1)
myLL.insertNode(0)
myLL.printLinkedList()

print(myLL.isPalindrome(myLL.head))

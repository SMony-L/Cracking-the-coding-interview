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
    # Values are stored in Reverse Order
    # input: 7->1->6 + 5->9->2 => 617+295
    # output: 2->1->9 => 912

    def sumList(self,l1,l2):
        # new dummy node 
        result = ListNode()

        curr = result
        carry = 0
        while l1 or l2:

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            value = v1 + v2 + carry

            carry = value // 10
            value %= 10
            
            curr.next = ListNode(value)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
            # Keep track of head 
            self.head = curr if not self.head else result.next
            
        return result.next

    # Follow Up #1 (Reverse LinkedList)
    # Values are stored in Forward Order
    # input: 6->1->7 + 2->9->5 => 617 + 295
    # output: 9->1->2

    # reverse the linked lists  
    # then sum the two lists like it is stored in reversed order  
    def reverse(self):
        curr = self.head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def getLen(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    # Follow Up #2 (Without Reverse the LinkedList)
    def sumListFollowUp(self,l1,l2, length1, length2):
        
        # check if the length are not the same
        if (length1 < length2):
            for i in range(length2 - length1):
                temp = ListNode(0)
                temp.next = l1
                l1 = temp
        else:
            for i in range(length1 - length2):
                temp = ListNode(0)
                temp.next = l2
                l2 = temp

        result = 0
        while l1 and l2:
            result = (result * 10) + l1.val + l2.val
            l1 = l1.next
            l2 = l2.next

        # result linked list
        ll = ListNode()
        # add the values to the result linked list
        for i in range(len(str(result)) - 1, -1, -1):
            ll = self.insertNode(str(result)[i])
        
        return ll
        

firstList = Solution()
secondList = Solution()

# Values are stored in-order

firstList.insertNode(7)
firstList.insertNode(1)
firstList.insertNode(6)
secondList.insertNode(5)
secondList.insertNode(9)
secondList.insertNode(2)

# Values are stored reversed order

# firstList.insertNode(6)
# firstList.insertNode(1)
# firstList.insertNode(7)
# secondList.insertNode(2)
# secondList.insertNode(9)
# secondList.insertNode(5)

print('First List = ')
firstList.printLinkedList()
len1 = firstList.getLen()

# For values that stored in-order

# print('Reversed First  List = ')
# firstList.reverse()
# firstList.printLinkedList()

print('Second List = ')
secondList.printLinkedList()
len2 = secondList.getLen()

# For values that stored in-order

# print('Reversed Second List = ')
# secondList.reverse()
# secondList.printLinkedList()

# Solution for Method 1 and Follow Up #1
# res = Solution()
# res.sumList(firstList.head, secondList.head)
# print('Result List = ')
# res.printLinkedList()


# Solution for Follow Up #2
res1 = Solution()
res1.sumListFollowUp(firstList.head, secondList.head, len1, len2)
print('Result List = ')
res1.printLinkedList()
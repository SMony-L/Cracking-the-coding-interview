class ListNode:
    def __init__ (self, val = 0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.head = None
        
    # insertNode from the front (head node)
    def insertNode(self,data):
        newNode = ListNode(data)
        newNode.next = self.head
        self.head = newNode
    
    def removeDups(self,ll):
        if ll.head is None:
            return
        # create a temp node point to head
        temp = ll.head
        # set to store all the value
        # start by store the value of head node
        mySet = set([temp.val])

        # while temp != null
        while (temp.next is not None):
            # if the value in the set
            # detact the linked between temp to temp->next and link from temp to temp->next->next
            if (temp.next.val in mySet):
                temp.next = temp.next.next
            else: 
            # if the value not in the set
            # add to the set
            # move to temp to the next node
                mySet.add(temp.next.val)
                temp = temp.next
        # return the linked list
        return ll
        
    def printLinkedList(self):
        curr = self.head
        while (curr):
            print(curr.val)
            curr = curr.next


firstList = Solution()

firstList.insertNode(5)
firstList.insertNode(7)
firstList.insertNode(5)
firstList.insertNode(8)
firstList.printLinkedList()
print("---")
firstList.removeDups(firstList)
firstList.printLinkedList()


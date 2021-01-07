class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Queue:
    def __init__(self):
        self.first = self.last = None
    
    # Check if Queue is Empty
    def isEmpty(self):
        return self.first == None

    # EnQueue
    def add(self,data):
        temp = ListNode(data)

        if self.last is None:
            self.first = self.last = temp
            return
        self.last.next = temp
        self.last = temp
    
    # DeQueue
    def remove(self):
        if self.isEmpty():
            return

        temp = self.first
        self.first = temp.next

        if self.first == None:
            self.last = None

    # display Queue
    def printQueue(self):
        curr = self.first
        while curr:
            print(curr.val, '->', end=' ')
            curr = curr.next

    # Look at front of the Queue
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.first.val


myQ = Queue()

# 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None
# Front = 0
myQ.add(0)
myQ.add(1)
myQ.add(2)
myQ.add(3)
myQ.add(4)
myQ.add(5)
myQ.printQueue()

print('\nFront Value is {}'.format(myQ.peek()))

# 1 -> 2 -> 3 -> 4 -> 5
# Front = 1
myQ.remove()
myQ.printQueue()
print('\nFront Value is {}'.format(myQ.peek()))

# 4 -> 5
# Front = 4
myQ.remove()
myQ.remove()
myQ.remove()
myQ.printQueue()
print('\nFront Value is {}'.format(myQ.peek()))
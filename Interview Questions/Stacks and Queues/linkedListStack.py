# Implementing a stack using LinkedList

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    

class Stack:
    def __init__(self):
        self.head = None
    
    # check if stack is empty
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
        
    # add item to stack
    def push(self,data):
        newNode = ListNode(data)
        newNode.next = self.head
        self.head = newNode

    # pop item off the stack
    def pop(self):
        if self.head is None:
            return None
        else:
            poppedNode = self.head
            self.head = self.head.next
            poppedNode.next = None

            return poppedNode.val
    
    # peek at the top data
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.head.val

    # display stack
    def printStack(self):
        curr = self.head
        while curr:
            print(curr.val, '->', end=' ')
            curr = curr.next
            
            

myStack = Stack()
# Empty Stack
print(myStack.isEmpty())

# 5 -> 4 -> 3 -> 2 -> 1 -> 0 -> None
myStack.push(0)
myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)
myStack.push(5)

# The Top Value is 5
print(myStack.printStack())
print('The Top Value is {}'.format(myStack.peek()))

# Stack is not Empty
print(myStack.isEmpty())

# 4 -> 3 -> 2 -> 1 -> 0 -> None
myStack.pop()
print(myStack.printStack())

# 2 -> 1 -> 0 -> None
# The Top Value is 2
myStack.pop()
myStack.pop()
print(myStack.printStack())
print('The Top Value is {}'.format(myStack.peek()))


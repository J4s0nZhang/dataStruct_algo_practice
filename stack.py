"""
Practice for implementing and using stacks and Queues in Python. 
Can use linked lists, but Python has much easier ways to implement
them nicely. 

Jason Zhang April 2020
"""

class Stack_List:
    """ Stack implemented using the list python data structure
    Shortcomings:
        1): Index Error if pop is called on an empty stack,
            which this class tries to fix with a warning that ignores it.
        2): Items stored next to each other in memory, which means if stack is larger
            than the memory block holding it, then some append() calls will take
            longer than others
    """
    def __init__(self):
        self.stack = []
        self.size = 0 
    
    def push(self, val=None):
        self.stack.append(val)
        self.size += 1
    
    def pop(self):
        val = None
        try:
            val = self.stack.pop()
        except IndexError:
            print("Warning: Attempted to pop from empty stack")
        return val
    
    def get_size(self):
        return self.size

"""
The second option of implementing a stack is to use the deque library
a deque is a "double-ended" queue 
"""
from collections import deque 

class Stack_Deque:
    """ Stack implemented using the deque python data structure
    Shortcomings:
        1): the exception error issue still presists, 
            I am addressing it the same way as in the Stack_list class with
            try/ except 
    Advantage:
        1): the deque data structure is created using a doubly linked list, therefore
            the memory allocation speed problem of lists is dealt with
    """
    def __init__(self):
        self.stack = deque()
        self.size = 0 
    
    def push(self, val=None):
        self.stack.append(val)
        self.size += 1
    
    def pop(self):
        val = None
        try:
            val = self.stack.pop()
        except IndexError:
            print("Warning: pop from empty stack")
        return val
    
    def get_size(self):
        return self.size

# testing
if __name__ == "__main__":
    print("stack list implementation")
    stack1 = Stack_List()
    print("pushing elements: ")
    stack1.push(1)
    stack1.push(12)
    print("size: " + str(stack1.get_size()))
    print("poped: " + str(stack1.pop()))
    print("size: " + str(stack1.get_size()))

    print("stack deque implementation")
    stack2 = Stack_Deque()
    print("pushing elements: ")
    stack2.push(1)
    stack2.push(12)
    print("size: " + str(stack2.get_size()))
    print("poped: " + str(stack2.pop()))
    print("size: " + str(stack2.get_size()))
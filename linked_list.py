"""
Singlely linked list and node structure implementation
in python practice (not sure how useful it will be with how nicely
python does data structures, but it's good practice)

Jason Zhang April 2020
"""

class Node:
    # Node implemented as a class as structures do not exist in python
    def __init__(self, val=None):
        """
        val sets the value of the node
        next pointer of the node defaults to None 
        """
        self.data = val 
        self.nextval = None

class LinkedList:
    """
    Singlely linkedlist class
    head: keeps track of first element of the list
    tail: keeps track of last element of the list
    size: keeps track of the size of the list
    """
    def __init__(self):
        self.head = None 
        self.size = 0 
        self.tail = None 

    def print_list(self):
        pointer = self.head 
        while pointer is not None:
            print(pointer.data)
            pointer = pointer.nextval 

    def add_node(self, val=None):
        new_node = Node(val)    
        if self.head is None:
            self.head = new_node
            self.tail = new_node 
            self.size += 1
        else:
            self.tail.nextval = new_node
            self.tail = new_node
            self.size += 1



# testing
if __name__ == "__main__":
    # testing add and print 
    linked_list = LinkedList()
    linked_list.add_node(1)
    linked_list.add_node(2)
    print("Added elements 1 and 2 to list")
    print("Contents of list:")
    linked_list.print_list()
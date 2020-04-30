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
    size: keeps track of the size of the list
    """
    def __init__(self):
        self.head = None 
        self.size = 0 

    def print_list(self):
        pointer = self.head 
        while pointer is not None:
            print(pointer.data)
            pointer = pointer.nextval 
    
    
    def append_node(self, val=None):
        """ Inserts a node to the end of the linked list
        """
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.size += 1
        else:
            pointer = self.head
            while pointer.nextval is not None:
                pointer = pointer.nextval
            tail = pointer
            tail.nextval = new_node
            tail = new_node
            self.size += 1
        return


    def insert_node(self, val=None, pos_val=None):
        """ Inserts a node at specified location
        If no location is given or no such location found,
        insert node at the end of the list 
        
        Args:
            val: the data value of the new node 
            pos_val: the value of the node that the new node should be inserted after
        """ 
        if pos_val is not None: 
            pointer = self.head
            search = True
            while search:
                if pointer is None:
                    search = False
                elif pointer.data == pos_val:
                    search = False
                else:
                    pointer = pointer.nextval

            if pointer.nextval is not None:
                new_node = Node(val)  
                temp = pointer.nextval 
                pointer.nextval = new_node
                new_node.nextval = temp 
                self.size += 1
            else:
                # position value was not found, appending val to end of list
                self.append_node(val) 
        else:
            # no positional value given and list isn't empty, append val to end of list 
            self.append_node(val)
        
        return


    def remove_node(self, val=None):
        # if the list is empty do nothing 
        if self.head is None:   
            return 
        # if we are deleting the head 
        if self.head.data == val:   
            temp = self.head.nextval
            self.head = None 
            self.head = temp 
            self.size -= 1
            return 
        else:
            # iterate through the list and get the node before the node to be deleted 
            pointer = self.head
            while pointer.nextval is not None and pointer.nextval.data != val:
                pointer = pointer.nextval
            if pointer.nextval is None: 
                return
            else:
                temp = pointer.nextval 
                pointer.nextval = temp.nextval 
                temp = None 
                self.size -= 1
                return 
    
    def get_size(self):
        return self.size 
        
           
# testing
if __name__ == "__main__":
    # testing add and print 
    linked_list = LinkedList()
    linked_list.insert_node(1)
    linked_list.append_node(2)
    linked_list.insert_node(4,1)
    print("Added elements to list")
    print("Contents of list:")
    linked_list.print_list()
    print("size: " + str(linked_list.get_size()))
    linked_list.remove_node(2)
    linked_list.remove_node(1)
    linked_list.remove_node(4)
    print("Removed node")
    print("Contents of list:")
    linked_list.print_list()
    print("size: " + str(linked_list.get_size()))
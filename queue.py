"""
Practice for implementing python queues
List and deque versions implemented as classes 
Probably the best choice to use dequeue for stack and queue implementations in
python, but using a list to practice pointers 

Jason Zhang April 2020 
"""
from collections import deque 


class Queue_List:
    """ Class implements a queue in a list in a circular fashion
    maximum size N is required
    """
    def __init__(self, max_len):
        self.max = max_len + 1
        self.queue = [None] * self.max
        # front and rear index pointers are what gives the queue a circular nature
        self.front = 0
        self.rear = 0 
        self.size = 0 


    def isEmpty(self):
        return self.size == 0 


    def enqueue(self, val):
        if self.size == self.max - 1:
            print("Error: queue is full")
        else:
            self.queue[self.front] = val 
            self.front = (self.front + 1) % self.max
            self.size += 1 

        return 


    def dequeue(self):
        val = None 
        if self.isEmpty():
            print("Error: cannot dequeue from empty enqueue")
        else:
            val = self.queue[self.rear]
            self.queue[self.rear] = None
            self.rear = (self.rear + 1) % self.max 
            self.size -= 1
        return val 


    def print_queue(self):
        for value in self.queue:
            if value is not None: 
                print(value)


if __name__ == "__main__":
    queue1 = Queue_List(5)
    print(queue1.isEmpty())
    queue1.enqueue(1)
    queue1.enqueue(2)
    queue1.enqueue(3)
    queue1.enqueue(4)
    queue1.print_queue()
    print("dequeued: " + str(queue1.dequeue()))
    print("dequeued: " + str(queue1.dequeue()))
    queue1.print_queue()
    queue1.enqueue(1)
    queue1.enqueue(2)
    print("dequeued: " + str(queue1.dequeue()))
    print("dequeued: " + str(queue1.dequeue()))
    

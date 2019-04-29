#!/bin/python3

class Queue(object):
    """
    Array implementation of a queue.
    """
    def __init__(self, n):
        """
        Allocate memory for a queue of at most n-1 elements.
        """
        self.n = n
        self.Q = [None]*n
        self.head = 0
        self.tail = 0

    @property
    def is_empty(self):
        """
        Return True if queue is empty (head=tail), else return
        False.
        """
        return self.head == self.tail

    def enqueue(self, x):
        """
        Add element x to queue.

        Args:
            x (int)
        """
        if (self.tail + 1) % self.n == self.head:
            raise AssertionError("Queue overflow")
        self.Q[self.tail] = x
        self.tail = (self.tail + 1) % self.n

    def dequeue(self):
        """
        Return element from queue in FIFO order.
        
        Returns: 
            int
        """
        if self.is_empty:
            raise AssertionError("Queue underflow!")
        x = self.Q[self.head]
        self.head = (self.head + 1) % self.n
        return x


class Deque(Queue):
    """
    Array implementation of a deque (double-ended queue).
    Allow insertion and deletion at both ends in O(1) time.
    
    CLRS Exercise 10.1-5
    """
    def insert_right(self, x):
        """
        Insert element x at right end of deque.
        
        Args:
            x (int)
        """
        if (self.tail + 1) % self.n == self.head:
            raise AssertionError("Overflow")
        self.Q[self.tail] = x
        self.tail = (self.tail + 1) % self.n

    def insert_left(self, x):
        """
        Insert element x at left end of deque.
        
        Args:
            x (int)
        """
        if self.head == 0:
            head_new = self.n-1
        else:
            head_new = self.head-1
        if head_new == self.tail:
            raise AssertionError("Overflow")
        self.Q[head_new] = x
        self.head = head_new

    def delete_right(self):
        """
        Delete element from right end of deque.
        
        Returns:
            int
        """
        if self.is_empty:
            raise AssertionError("Underflow!")
        if self.tail == 0:
            tail_new = self.n-1
        else:
            tail_new = self.tail-1
        x = self.Q[tail_new]
        self.Q[tail_new] = None
        self.tail = tail_new
        return x

    def delete_left(self):
        """
        Delete element from left end of deque.
        
        Returns:
            int
        """
        if self.is_empty:
            raise AssertionError("Underflow!")
        x = self.Q[self.head]
        self.Q[self.head] = None
        self.head = (self.head + 1) % self.n
        return x




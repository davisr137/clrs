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

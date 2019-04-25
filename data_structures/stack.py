#!/bin/python3

class Stack(object):
    """
    Array implementation of a stack.
    """
    def __init__(self, n=10):
        """
        Allocate memory for list representing stack.

        Args:
            n (int): Maximum number of elements in stack.
        """
        self.n = n
        self.S = [None]*n
        self.top = -1

    @property
    def stack_empty(self):
        """
        Return True if stack is empty (top=0), otherwise
        return False.
        """
        if self.top == -1:
            return True
        else:
            return False

    def push(self, x):
        """
        Insert an element onto the top of the stack.
        
        Args:
            x (int): Element to insert.
        """
        if self.top >= self.n-1:
            raise AssertionError("Stack overflow!")
        self.top += 1
        self.S[self.top] = x

    def pop(self):
        """
        Pop element from top of stack. 
        """
        if self.stack_empty:
            raise AssertionError("Stack underflow!")
        self.top -= 1
        return self.S[self.top + 1]
    


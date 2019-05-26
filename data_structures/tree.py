import math
from typing import List

## CLRS Chapter 12: Binary Search Trees

class BinaryNode:
    """
    Class for node in binary search tree.
    """
    def __init__(self, val: int):
        """
        Constructor. Key is given by val.
        """
        self.val = val
        self.p = None # Parent
        self.left = None # Left child
        self.right = None # Right child
    def add_parent(self, parent):
        """
        Add parent.
        """
        self.parent = parent
    def add_left(self, left):
        """
        Add left child. 
        """
        if left.val > self.val:
            s = "Left child value must be less than or equal to node value."
            raise AssertionError(s)
        self.left = left
    def add_right(self, right):
        """
        Add right child.
        """
        if right.val < self.val:
            s = "Right child value must be greater than or equal to node value."
            raise AssertionError(s)
        self.right = right

def array_to_bst(arr: List[int]) -> BinaryNode:
    """
    Convert sorted array to binary search tree.
    """
    if not arr:
        return None
    # Make root from midpoint of array
    L = len(arr)
    mid = math.floor(L/2)
    root = BinaryNode(arr[mid])
    # Recursively call function on left and right arrays
    left_half = arr[:mid]
    if left_half:
        left = array_to_bst(left_half)
        root.add_left(left)
    right_half = arr[mid+1:]
    if right_half:
        right = array_to_bst(right_half)
        root.add_right(right)
    return root

def inorder_tree_walk(node: BinaryNode) -> None:
    """
    Perform an in-order tree walk / traversal.
    """
    if node:
        inorder_tree_walk(node.left)
        print(node.val)
        inorder_tree_walk(node.right)

def preorder_tree_walk(node: BinaryNode) -> None:
    """
    Perform a pre-order tree walk / traversal.
    """
    if node:
        print(node.val)
        inorder_tree_walk(node.left)
        inorder_tree_walk(node.right)

def postorder_tree_walk(node: BinaryNode) -> None:
    """
    Perform a post-order tree walk / traversal.
    """
    if node:
        inorder_tree_walk(node.left)
        inorder_tree_walk(node.right)
        print(node.val)

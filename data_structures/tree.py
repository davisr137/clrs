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
        self.parent = None # Parent
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
        left.add_parent(root)
        root.add_left(left)
    right_half = arr[mid+1:]
    if right_half:
        right = array_to_bst(right_half)
        right.add_parent(root)
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

def tree_search(node: BinaryNode, val: int) -> int:
    """
    Search for node with value val in tree.
    """
    if not node:
        return None
    if node.val == val: # Found node!
        return node
    if val < node.val: # Go left
        return tree_search(node.left, val)
    else: # Go right
        return tree_search(node.right, val)

def tree_minimum(root: BinaryNode) -> BinaryNode:
    """
    Get node with minimum value in BST.
    """
    node = root
    while node.left:
        node = node.left
    return node

def tree_maximum(root: BinaryNode) -> BinaryNode:
    """
    Get node with maximum value in BST.
    """
    node = root
    while node.right:
        node = node.right
    return node

def tree_successor(node: BinaryNode) -> BinaryNode:
    """
    Get successor to node in BST.
    """
    if node.right:
        return tree_minimum(node.right)
    x = node
    y = node.parent
    while y:
        if x != y.right:
            break
        x = y
        y = y.parent
    return y

def tree_insert(root: BinaryNode, z: int) -> None:
    """
    Insert a node with value z into a BST.
    """
    # Start with y as None and x pointing to root
    y = None
    x = root
    # Trace down tree until y is a leaf
    while x:
        y = x
        if z < x.val:
            x = x.left
        else:
            x = x.right
    # Create a node with value z
    z_node = BinaryNode(z)
    z_node.add_parent(y)
    # Add z as child of y
    if y:
        if z < y.val:
            y.add_left(z_node)
        else:
            y.add_right(z_node)

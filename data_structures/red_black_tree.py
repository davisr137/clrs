from tree import BinaryNode

# CLRS Chapter 13: Red-Black Trees

class RedBlackNode(BinaryNode):
    """
    Class for node in a red-black tree. Inherit from the
    binary search tree node class.
    """
    def __init__(self, val: int):
        """
        Constructor. Key is given by val.
        """
        self.val = val
        # Parent, left child, right child
        self.parent = None
        self.left = None
        self.right = None
        # Color of node (either red or black)
        self.color = None
    def add_color(self, color: str):
        """
        Add color (R or B) to node.
        """
        if color not in set(['R', 'B']):
            raise AssertionError('Color must be R or B!')
        self.color = color

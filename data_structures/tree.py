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
        self.left_child = None # Left child
        self.right_child = None # Right child
    def add_parent(self, parent: BinaryNode):
        """
        Add parent.
        """
        self.parent = parent
    def add_left_child(self, left_child: BinaryNode):
        """
        Add left child. 
        """
        if left_child.val > self.val:
            s = "Left child value must be less than or equal to node value."
            raise AssertionError(s)
        self.left_child = left_child
    def add_right_child(self, right_child: BinaryNode):
        """
        Add right child.
        """
        if right_child.val < self.val:
            s = "Right child value must be greater than or equal to node value."
            raise AssertionError(s)


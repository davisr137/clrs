from typing import List

class LinkedListNode():
    """
    Node in linked list.
    """ 
    def __init__(self, val: int):
        self.val = val
        self.prev = None
        self.next = None

def build_linked_list_from_array(array: List[int]) -> LinkedListNode:
    """
    Build (doubly) linked list from array. Return head of linked list.
    """
    head = None
    for val in array:
        if not head:
            head = LinkedListNode(val)
            node = head
        else:
            prev = node
            node.next = LinkedListNode(val)
            node = node.next
            node.prev = prev
    return head

def list_search(head: LinkedListNode, k: int) -> LinkedListNode:
    """
    Search linked list for node with value k.
    """
    node = head
    while node.val != k:
        node = node.next
        if not node:
            return None
    return node

def list_insert(head: LinkedListNode, x: LinkedListNode) -> LinkedListNode:
    """
    Insert node x into the front of a (doubly) linked list. 
    x becomes the head of the list.
    """
    x.next = head
    if head:
        head.prev = x
    return x

def list_delete(node: LinkedListNode) -> None:
    """
    Delete node x from linked list.
    """
    if node.prev:
        node.prev.next = node.next
    if node.next:
        node.next.prev = node.prev

## Use a sentinel to simplify boundary conditions.

def get_linked_list_tail(head: LinkedListNode) -> LinkedListNode:
    """
    Get tail of linked list.
    """
    tail = head
    while tail.next:
        tail = tail.next
    return tail

def build_linked_list_with_sentinel(array: List[int]) -> LinkedListNode:
    """
    Build a linked list with sentinel from an array.
    """
    # Head and tail
    head = build_linked_list_from_array(array)
    tail = get_linked_list_tail(head)
    # Add sentinel
    sentinel = LinkedListNode(None)
    head.prev = sentinel
    tail.next = sentinel
    sentinel.prev = tail
    sentinel.next = head
    return head

## Exercises

## 10.2-7: Reverse a singly linked list of n elements. Use no more than
## constant storage beyond that needed for the list itself.

def build_singly_linked_list(array: List[int]) -> LinkedListNode:
    """
    Build (singly) linked list from array. Return head of linked list.
    """
    head = None
    for val in array:
        if not head:
            head = LinkedListNode(val)
            node = head
        else:
            node.next = LinkedListNode(val)
            node = node.next
    return head

def reverse_singly_linked_list(node):
    """
    Reverse a singly linked list. Return head of reversed list. 

    Uses O(1) space. Maintains pointers to three nodes in memory.
    * previous node
    * current node
    * next node
    """
    # First node in list
    prev = node
    curr = node.next
    next_ = node.next.next
    curr.next = prev
    # Previous head becomes tail
    prev.next = None
    # Iterate through list
    while next_:
        prev = curr
        curr = next_
        next_ = next_.next
        curr.next = prev
    # Return head of reversed list
    return curr

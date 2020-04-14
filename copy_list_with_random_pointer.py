"""
138. Copy List with Random Pointer
https://leetcode.com/problems/copy-list-with-random-pointer/
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        copy_head = Node(head.val)
        pointer = head
        copy_pointer = copy_head
        node_mapping = {}
        # build the linked list
        while pointer:
            node_mapping[pointer] = copy_pointer
            if pointer.next:
                copy_pointer_next = Node(pointer.next.val)
            else:
                copy_pointer_next = None

            copy_pointer.next = copy_pointer_next
            pointer = pointer.next
            copy_pointer = copy_pointer.next
        # build the random pointer
        pointer = head
        copy_pointer = copy_head
        while pointer:
            if pointer.random is not None:
                copy_pointer.random = node_mapping[pointer.random]
            pointer = pointer.next
            copy_pointer = copy_pointer.next
        return copy_head
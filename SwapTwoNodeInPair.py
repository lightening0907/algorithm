# Given a linked list, swap every two adjacent nodes and return its head.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        N1 = head.next
        N2 = head
        N2.next = self.swapPairs(N1.next)
        N1.next = N2
        return N1
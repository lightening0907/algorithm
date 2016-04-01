"""
Given a list, rotate the list to the right by k places,
where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k==0 or not head: return head
        node = head
        len_list = 1
        while node.next:
            len_list +=1
            temp_node = node.next
            node = temp_node
        tail = node
        k_p = k%len_list
        if k_p == 0: return head
        tail.next = head
        node = head
        for i in range(len_list-k_p-1):
            temp_node = node.next
            node = temp_node
        new_head = node.next
        node.next = None
        return new_head
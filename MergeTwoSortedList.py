# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # temp_ln = ListNode()
        # ret_list = []
        pre_temp = None
        if not l1 and not l2: return []
        while l1 or l2:
            while l1 and (not l2 or l1.val<=l2.val):
                temp = ListNode(l1.val)
                if pre_temp:
                    pre_temp.next = temp
                else:
                    first_node = temp
                pre_temp = temp
                l1 = l1.next
            while l2 and (not l1 or l1.val>l2.val):
                temp = ListNode(l2.val)
                if pre_temp:
                    pre_temp.next = temp
                else:
                    first_node = temp
                pre_temp = temp
                l2 = l2.next
        return first_node

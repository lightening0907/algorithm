# Given a linked list, remove the nth node from the end of list and return its head.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        i = 0
        dict_Node ={}
        temp = head
        while temp:
            dict_Node[i] = temp
            temp = temp.next
            i+=1
        if i==n and i>1: return dict_Node[1]
        if i==n and i==1: return None
        if n>1:
            dict_Node[i-n-1].next = dict_Node[i-n+1]
        elif i>=2 and n==1:
            dict_Node[i-2].next = None
        return head
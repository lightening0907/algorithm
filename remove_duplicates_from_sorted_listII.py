"""
Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        dummy = ListNode(0)
        Node = head
        pt = dummy
        repeated = 0
        while (Node and Node.next):
            if Node.next.val != Node.val:
                if repeated == 0:
                    pt.next = Node
                    pt = Node
                repeated = 0
            else:
                repeated = 1
            Node = Node.next
        if repeated ==1:
            pt.next = None
        else:
            pt.next = Node
        return dummy.next

Node1 = ListNode(1)
Node2 = ListNode(1)
Node3 = ListNode(2)
Node4 = ListNode(2)
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Solution1 = Solution()
print Solution1.deleteDuplicates(Node1).val
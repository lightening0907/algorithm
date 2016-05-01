"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        root = head
        try:
            cycle_len = 1
            node = head.next
            node2 = head.next.next
            while node !=node2:
                node = node.next
                node2 = node2.next.next
                cycle_len += 1
            while root != node2:
                root = root.next
                node2 = node2.next
            return root

        except:
            return None

ln1 = ListNode(3)
ln2 = ListNode(2)
ln3 = ListNode(0)
ln4 = ListNode(-4)
ln1.next = ln2
ln2.next = ln3
ln3.next = ln4
ln4.next = ln2

Solutions = Solution()
Solutions.detectCycle(ln1)
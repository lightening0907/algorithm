# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head: return
        node = head
        linked = [node]
        while node.next:
         node = node.next
         linked.append(node)
        node = head
        for i in range(len(linked)-1,len(linked)//2,-1):
            temp_node_next = node.next
            node.next = linked[i]
            linked[i].next = temp_node_next
            linked[i-1].next = None
            node = temp_node_next
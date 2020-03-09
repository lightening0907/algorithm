# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        index = 0
        next_value = 0
        while True:
            temp_value = l1.val + l2.val + next_value
            current_value = temp_value % 10
            next_value = temp_value // 10
            current_node = ListNode(current_value)
            if index == 0:
                previous_node = current_node
                return_node = previous_node
            else:
                previous_node.next = current_node
                previous_node = current_node
            if l1.next is not None:
                l1 = l1.next
            else:
                l1.val = 0
            if l2.next is not None:
                l2 = l2.next
            else:
                l2.val = 0
            if (l1.next is None) and (l2.next is None) and (l2.val + l1.val + next_value == 0):
                return return_node
            index += 1


class Solution2020(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur_val = (l1.val + l2.val) % 10
        next_val =(l1.val + l2.val) // 10
        outputNode = ListNode(cur_val)
        currentNode = outputNode
        while next_val > 0 or l1.next or l2.next:
            if l1.next:
                l1 = l1.next
                next_val += l1.val
            if l2.next:
                l2 = l2.next
                next_val +=l2.val
            cur_val = next_val%10
            next_val = next_val //10
            NextNode = ListNode(cur_val)
            currentNode.next = NextNode
            currentNode = NextNode
        return outputNode

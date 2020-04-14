# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        tail, new_head = self.find_tail_new_head(head)
        self.quick_sort(head, None, tail)
        return new_head


    def find_tail_new_head(self, head):
        new_head = head
        pointer = head
        # parent_of_tail = None
        while pointer:
            if pointer.val < new_head.val:
                new_head = pointer
            if pointer.next is None:
                tail_pointer = pointer
                pointer = pointer.next
            else:
                # parent_of_tail = pointer
                pointer = pointer.next
        return tail_pointer, new_head

    def switch_nodes(self, pointer_1, pointer_1_parent, pointer_2, pointer_2_parent):

        if pointer_1_parent:
            pointer_1_parent.next = pointer_2

        if pointer_2_parent != pointer_1:
            # two node are not next to each other
            pointer_2_parent.next = pointer_1
            pointer_2.next, pointer_1.next = pointer_1.next, pointer_2.next
        else:
            pointer_2_parent = pointer_2
            pointer_2.next, pointer_1.next = pointer_1, pointer_2.next

        pointer_1, pointer_2  = pointer_2, pointer_1
        return pointer_1, pointer_2, pointer_1_parent, pointer_2_parent

    def partition(self, left_node, left_node_parent, right_node):
        pointer_1 = left_node
        pointer_1_parent = left_node_parent
        pointer_2 = left_node
        pointer_2_parent = left_node_parent
        while pointer_2 != right_node:
            if pointer_2.val <= right_node.val:
                # switch pointer1 and pointer 2
                if pointer_2.next == right_node:
                    right_node_parent = pointer_1
                if pointer_1 != pointer_2:
                    if pointer_1 == left_node:
                        left_node = pointer_2
                        if left_node_parent:
                            left_node_parent.next = pointer_2


                    pointer_1, pointer_2, pointer_1_parent, pointer_2_parent = self.switch_nodes(pointer_1, pointer_1_parent, pointer_2, pointer_2_parent)
                pointer_1_parent, pointer_1, pointer_2_parent, pointer_2 = pointer_1, pointer_1.next, pointer_2, pointer_2.next
            else:
                if pointer_2.next == right_node:
                    right_node_parent = pointer_2
                pointer_2_parent, pointer_2 = pointer_2, pointer_2.next

        # switch pointer 1 and right_node
        if pointer_1 == left_node:
            left_node = right_node
            if left_node_parent:
                left_node_parent.next = right_node
        pointer_1, right_node, pointer_1_parent, right_node_parent =  self.switch_nodes(pointer_1, pointer_1_parent, right_node, right_node_parent)
        return pointer_1, pointer_1_parent, left_node, left_node_parent, right_node, right_node_parent

    def quick_sort(self, left_node, left_node_parent, right_node):
        if left_node != right_node:
            pointer_1, pointer_1_parent, left_node, left_node_parent, right_node, right_node_parent = self.partition(left_node, left_node_parent, right_node)
            if left_node != pointer_1 and pointer_1_parent != left_node:
                self.quick_sort(left_node, left_node_parent, pointer_1_parent)
            if pointer_1!= right_node and pointer_1.next != right_node:
                self.quick_sort(pointer_1.next, pointer_1, right_node)

val_list = [1,3,]
for val_index, val in enumerate(val_list):
    if val_index == 0:
        node = ListNode(val)
        root = node
    if val_index < len(val_list) - 1:
        node_next = ListNode(val_list[val_index + 1])
        node.next = node_next
        node = node_next


solution = Solution()
print(solution.sortList(root))
                 
        
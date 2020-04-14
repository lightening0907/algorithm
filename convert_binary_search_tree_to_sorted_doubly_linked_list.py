"""
426. Convert Binary Search Tree to Sorted Doubly Linked List
https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        if root.left:
            left = self.treeToDoublyList(root.left)
            if root.right:
                right = self.treeToDoublyList(root.right)
                # left.left #largest element in left dl
                # right.left #largest element in right dl
                left.left.right = root
                root.left = left.left
                root.right = right
                left.left  = right.left
                right.left.right = left
                right.left = root
            else:
                left.left.right = root
                root.left = left.left
                left.left = root
                root.right = left
            return left
        else:
            if root.right:
                right = self.treeToDoublyList(root.right)
                # left.left #largest element in left dl
                # right.left #largest element in right dl
                right.left.right = root
                root.left = right.left
                root.right = right
                right.left = root
            else:
                root.left = root
                root.right = root
            return root

node = Node(1)
solution = Solution()
ans = solution.treeToDoublyList(node)
print(ans.val)

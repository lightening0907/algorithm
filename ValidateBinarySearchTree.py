# Given a binary tree, determine if it is a valid binary search tree (BST).
"""
Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root): #BST traversal inorder has to be a increasing sequence
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        stack = []
        trav_inorder = []
        node = root
        while True:
            while(node):
                stack.append(node)
                node = node.left
            if not stack: return True
            else:
                node = stack.pop()
            #if not node: return True
            if trav_inorder and node.val <= trav_inorder[-1]:
                return False
            else:
                trav_inorder.append(node.val)

            #if node.right:
            #    stack.append(node.right)
            node = node.right
            # if not stack: return True

Node1 = TreeNode(0)
Node2 = TreeNode(1)
Node1.right = Node2
Solution1 = Solution()
print Solution1.isValidBST(Node1)
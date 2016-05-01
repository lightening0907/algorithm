# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return root
        list_node = []
        while root:
            list_node.append(root)
            root = root.left
        root = list_node.pop()
        node = root
        while list_node:
            right_node = list_node.pop()
            node.right = right_node
            node.left = right_node.right
            right_node.left = None
            right_node.right = None
            node = right_node
        return root

Node1 = TreeNode(1)
Node2 = TreeNode(2)
Node1.left = Node2

Solution1 = Solution()
Solution1.upsideDownBinaryTree(Node1)
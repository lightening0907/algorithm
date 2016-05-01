# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        prev_level = [root]
        this_level = []
        level_order = []
        while prev_level:
            prev_level_value = []
            this_level = []
            for node in prev_level:
                if node.left: this_level.append(node.left)
                if node.right: this_level.append(node.right)
                prev_level_value.append(node.val)
            # if not prev_level_value: return level_order
            level_order.append(prev_level_value)

            prev_level = this_level
        return level_order

Node1 = TreeNode(1)
Node2 = TreeNode(2)
Node1.left = Node2

Solution1 = Solution()
print Solution1.levelOrder(Node1)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        prev_level = [root]
        zigzag = []
        left_to_right = True
        while prev_level:
            this_level = []
            prev_level_value = []
            if left_to_right:
                for node in prev_level:
                    if node.left:
                        this_level.append(node.left)
                    if node.right:
                        this_level.append(node.right)
                    prev_level_value.append(node.val)
            else:
                for node in prev_level[::-1]:
                    if node.right:
                        this_level.insert(0,node.right)
                    if node.left:
                        this_level.insert(0,node.left)
                    prev_level_value.append(node.val)
            zigzag.append(prev_level_value)
            prev_level = this_level
            left_to_right = (not left_to_right)
        return zigzag
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

TreeNode1 = TreeNode(1)
TreeNode2 = TreeNode(2)
TreeNode3 = TreeNode(2)
TreeNode1.left = TreeNode2
TreeNode1.right = TreeNode3

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        parent = [root]
        while parent:
            child = []
            for parent_node in parent:
                if parent_node:
                    child.append(parent_node.left)
                    child.append(parent_node.right)

            if not child: break
            len_child = len(child)
            for i in range(len_child/2):
                if (not child[i] and child[len_child-1-i]) or (child[i] and not child[len_child-1-i]) or ((child[i] and child[len_child-1-i]) and child[i].val != child[len_child-1-i].val):
                    return False
            parent = child
        return True
Solution1 = Solution()
print Solution1.isSymmetric(TreeNode1)
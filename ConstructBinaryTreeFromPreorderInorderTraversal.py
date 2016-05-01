# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        len_node = len(preorder)
        if len_node == 0: return None
        root = TreeNode(preorder[0])
        if len_node == 1: return root
        inorder_index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:1+inorder_index],inorder[0:inorder_index])
        root.right = self.buildTree(preorder[1+inorder_index:],inorder[inorder_index+1:])
        return root
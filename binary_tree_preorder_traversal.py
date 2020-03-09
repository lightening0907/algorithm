"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        dfs_list = [root]
        preorder_trav_list = []
        visited_dict = {}
        while len(dfs_list)>0:
            if dfs_list[-1] in visited_dict:
                node = dfs_list.pop()
                if node.right:
                    dfs_list.append(node.right)
            else:
                visited_dict[dfs_list[-1]] = 1
                preorder_trav_list.append(dfs_list[-1].val)
                if dfs_list[-1].left:
                    dfs_list.append(dfs_list[-1].left)
        return preorder_trav_list

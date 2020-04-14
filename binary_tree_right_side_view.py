"""
199. Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        cur_level = [root]
        rs_view = []
        len_level = len(cur_level)
        while len_level > 0:
            next_level = []
            for node_index, cur_node in enumerate(cur_level):
                if cur_node.left:
                    next_level.append(cur_node.left)
                if cur_node.right:
                    next_level.append(cur_node.right)
                if node_index == len_level - 1:
                    rs_view.append(cur_node.val)
            cur_level = next_level
            len_level = len(cur_level)
        return rs_view
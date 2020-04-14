"""
https://leetcode.com/problems/binary-tree-vertical-order-traversal/
314. Binary Tree Vertical Order Traversal
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:

Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        col_map = {} # map col index
        if root is None:
            return []
        curr_bfs_nodes = [root]
        curr_bfs_col = [0]
        next_bfs_nodes = [root]
        next_bfs_col = [0]
        while len(curr_bfs_nodes)>0:
            next_bfs_nodes = []
            next_bfs_col = []
            while len(curr_bfs_nodes)>0:
                pointer = curr_bfs_nodes.pop(0)
                pointer_col = curr_bfs_col.pop(0)
                if pointer_col in col_map:
                    col_map[pointer_col].append(pointer.val)
                else:
                    col_map[pointer_col] = [pointer.val]
                if pointer.left:
                    next_bfs_nodes.append(pointer.left)
                    next_bfs_col.append(pointer_col - 1)
                if pointer.right:
                    next_bfs_nodes.append(pointer.right)
                    next_bfs_col.append(pointer_col + 1)
            curr_bfs_nodes = next_bfs_nodes
            curr_bfs_col = next_bfs_col
        out_put = []
        for col_map_key in sorted (col_map.keys()):
            out_put.append(col_map[col_map_key])
        return out_put
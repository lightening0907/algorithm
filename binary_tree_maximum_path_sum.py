"""
124. Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # traverse the tree in post order
        node_map = {} # node : {value:, left sum max:, right sum  max: left_visited: right_visited}
        po_trav = [root]
        max_path_sum = None
        while len(po_trav) > 0:
            if po_trav[-1] in node_map:
                if node_map[po_trav[-1]]['left_visited'] and node_map[po_trav[-1]]['right_visited']:
                    max_sum = po_trav[-1].val
                    tmp_path_sum =  max_sum
                    if po_trav[-1].left:
                        if node_map[po_trav[-1].left]['max_sum'] >=0:
                            max_sum = po_trav[-1].val + node_map[po_trav[-1].left]['max_sum']
                            tmp_path_sum = max_sum
                    if po_trav[-1].right:
                        if node_map[po_trav[-1].right]['max_sum'] >=0:
                            if max_sum < po_trav[-1].val + node_map[po_trav[-1].right]['max_sum']:
                                max_sum = po_trav[-1].val + node_map[po_trav[-1].right]['max_sum']
                            tmp_path_sum = tmp_path_sum + node_map[po_trav[-1].right]['max_sum']
                    node_map[po_trav[-1]]['max_sum'] = max_sum
                    if tmp_path_sum > max_path_sum or max_path_sum is None:
                        max_path_sum = tmp_path_sum
                    po_trav.pop()
                elif not node_map[po_trav[-1]]['right_visited']:
                    node_map[po_trav[-1]]['right_visited'] = True
                    if po_trav[-1].right:
                        po_trav.append(po_trav[-1].right)
            else:
                node_map[po_trav[-1]] = {'value': po_trav[-1].val,
                                         'max_sum': None,
                                         'left_visited': True,
                                         'right_visited': False}
                if po_trav[-1].left:
                    po_trav.append(po_trav[-1].left)
        return max_path_sum
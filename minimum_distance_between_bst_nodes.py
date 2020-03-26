"""
783. Minimum Distance Between BST Nodes
Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \
    1   3

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
Note:

The size of the BST will be between 2 and 100.
The BST is always valid, each node's value is an integer, and each node's value is different.
This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # in order traversal the tree
        dfs = [root]
        in_order_list = []
        visited = {}
        while len(dfs) > 0:
            if dfs[-1] in visited:
                node = dfs.pop()
                in_order_list.append(node.val)
                if node.right:
                    dfs.append(node.right)
            else:
                visited[dfs[-1]] = True
                if dfs[-1].left:
                    dfs.append(dfs[-1].left)


        diff = None
        for index in range(1, len(in_order_list)):
            if diff is None:
                diff = in_order_list[index] - in_order_list[index-1]
            else:
                if diff>in_order_list[index] - in_order_list[index-1]:
                    diff=in_order_list[index] - in_order_list[index-1]
        return diff

tn = TreeNode(4)
tn2 = TreeNode(2)
tn3 = TreeNode(1)
tn4 = TreeNode(3)
tn5 = TreeNode(6)
tn.left = tn2
tn.right = tn5
tn2.left = tn3
tn2.right = tn4
solution = Solution()
print(solution.minDiffInBST(tn))

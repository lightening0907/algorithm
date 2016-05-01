"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        prev_val = [root.val]
        prev_node = [root]
        final_sum = 0
        while prev_node:
            cur_node = []
            cur_val = []
            for i in range(len(prev_val)):
                if not prev_node[i].left and not prev_node[i].right:
                    final_sum += prev_val[i]
                    continue
                if prev_node[i].left:
                    cur_node.append(prev_node[i].left)
                    cur_val.append(prev_val[i]*10+prev_node[i].left.val)
                if prev_node[i].right:
                    cur_node.append(prev_node[i].right)
                    cur_val.append(prev_val[i]*10+prev_node[i].right.val)
            prev_val = cur_val
            prev_node = cur_node
        return final_sum
Node1=TreeNode(9)
Solution1 = Solution()
print Solution1.sumNumbers(Node1)
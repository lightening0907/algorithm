# Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from copy import deepcopy

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0: return []
        dp = []
        for i in range(1,n+1):
            if i==1:
                dp.append(TreeNode(i))
            else:
                dp_temp = []
                for root in dp:
                    """ for each tree, you can always add the new node as the new root
                    or as a right child of each right node down the root and turn the original right child to left child
                    """
                    root_copy = deepcopy(root)
                    new_root = TreeNode(i)
                    new_root.left = root_copy
                    dp_temp.append(new_root)
                    node = root
                    while node:

                        temp_node_right = node.right
                        node.right = TreeNode(i)
                        node.right.left = temp_node_right
                        root_copy = deepcopy(root)
                        node.right = temp_node_right
                        node = node.right
                        dp_temp.append(root_copy)
                dp = dp_temp
        return dp

class Solution2(object): # dp[i,j] saves the list of trees contains value i to j
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0: return []
        dp = {}
        for i in range(1,n+1):
            dp[i,i] = [TreeNode(i)]
        if n == 1: return dp[1,1]
        for k in range(1,n): #build tree from size 2 to size n whose values are all continuous numbers
            for i in range(1,n-k+1):
                j = i + k
                dp[i,j] = []
                for val in range(i,j+1):
                    lefttree = [None] if val == i else dp[i,val-1]
                    righttree = [None] if val == j else dp[val+1,j]
                    for lst in lefttree:
                        for rst in righttree:
                            root = TreeNode(val)
                            root.left = lst
                            root.right = rst
                            dp[i,j].append(root)
        return dp[1,n]
Solution1 = Solution2()
Solution1.generateTrees(2)
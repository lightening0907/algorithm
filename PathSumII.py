# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root: return []
        stack = []
        list_path = []
        temp_path = []
        temp_sum = 0
        node = root
        flag = 0
        while True:
            while node:
                stack.append(node)
                temp_path.append(node)
                temp_sum += node.val
                node = node.left
            if not stack:
                return list_path
            node = stack.pop()
            # if not stack: flag += 1
            # node=node.right
            if not node.right and not node.left:
                if temp_sum == sum:
                    list_path.append([node.val for node in temp_path])
            if not node.right:
                while temp_path and stack and temp_path[-1] != stack[-1]:
                    temp_val = temp_path.pop()
                    temp_sum -= temp_val.val
            node = node.right
        return list_path

Node5 = TreeNode(5)
Node4 = TreeNode(4)
Node8 = TreeNode(8)
Node11 = TreeNode(11)
Node13 = TreeNode(13)
Node42 = TreeNode(4)
Node7 = TreeNode(7)
Node2 = TreeNode(2)
Node1 = TreeNode(1)
Node5.left = Node4
Node5.right = Node8
Node4.left = Node11
Node8.left = Node13
Node8.right = Node42
Node11.left= Node7
Node11.right = Node2
Node42.right = Node1

Solution1 = Solution()
print Solution1.pathSum(Node5,18)
# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root: return
        prev_level_1_node = root
        prev_level_1_node.next = None
        node = root

        while prev_level_1_node.left:
            prev_node = TreeLinkNode(0) # dummy
            cur_level_1_node = node.left
            while node:
                curr_level = node.left
                prev_node.next = curr_level
                curr_level.next = node.right
                curr_level = curr_level.next
                prev_node = curr_level
                node = node.next
            curr_level.next = None
            prev_level_1_node = cur_level_1_node
            node = cur_level_1_node
        return

Node0 = TreeLinkNode(0)
Node1 = TreeLinkNode(1)
Node2 = TreeLinkNode(2)
Node3 = TreeLinkNode(3)
Node4 = TreeLinkNode(4)
Node5 = TreeLinkNode(5)
Node6 = TreeLinkNode(6)
Node0.left = Node1
Node0.right = Node2
Node1.left = Node3
Node1.right = Node4
Node2.left = Node5
Node2.right = Node6

Solution1 = Solution()
Solution1.connect(Node0)
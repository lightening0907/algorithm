"""
Given a binary tree, return the inorder traversal of its nodes' values.
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal_rec(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)

class Solution2(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        list_node = [root]
        inorder_list = []
        visited_dict = {}
        while list_node:
            visited_dict[list_node[-1]]=1
            if list_node[-1].left and list_node[-1].left not in visited_dict:
                list_node.append(list_node[-1].left)
            else:
                temp_node = list_node[-1].right
                inorder_list.append(list_node[-1].val)
                del list_node[-1]
                if temp_node:
                    list_node.append(temp_node)
        return inorder_list


class Solution3(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        visited_map = {}
        if not root:
            return []
        dfs_list  = [root]
        inorder_trav_list = []
        while len(dfs_list) > 0:
            if  dfs_list[-1] in visited_map:
                node = dfs_list.pop()
                inorder_trav_list.append(node.val)
            else:
                visited_map[dfs_list[-1]] = 1
                if dfs_list[-1].right:
                    dfs_list = dfs_list[:-1] + [dfs_list[-1].right] + [dfs_list[-1]]
                if dfs_list[-1].left:
                    dfs_list = dfs_list + [dfs_list[-1].left]

        return inorder_trav_list
tr1 = TreeNode(1)
tr2 = TreeNode(2)
tr1.left=tr2
Solution1 = Solution2()
print Solution1.inorderTraversal(tr1)


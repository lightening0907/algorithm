# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.inorder = inorder
        self.num_node = len(self.inorder)
        self.postorder = postorder
        self.inorder_dict = {v:i for i,v in enumerate(self.inorder)}
        return self.build(0,self.num_node-1,0,self.num_node-1)

    def build(self,ist,iend,pst,pend):
        if iend<ist: return None
        root = TreeNode(self.postorder[pend])
        index_inorder = self.inorder_dict[self.postorder[pend]]
        root.left = self.build(ist,index_inorder-1,pst,pend-iend+index_inorder-1)
        root.right = self.build(index_inorder+1,iend,pend-iend+index_inorder,pend-1)
        return root

class Solution2(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) ==0:
            return None
        root_val = postorder[-1]
        for i_index in range(len(inorder)):
            if inorder[i_index] == root_val:
                left_branch = self.buildTree(inorder[:i_index], postorder[:i_index])
                right_branch = self.buildTree(inorder[i_index + 1:], postorder[i_index:-1])
        root = TreeNode(root_val)
        root.left = left_branch
        root.right = right_branch
        return root
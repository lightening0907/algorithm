"""
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

"""
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:return 0
        node_range = range(1,n+1)
        self.dict_num_tree = {}
        return self.find_bst(node_range)

    def find_bst(self,node_val_list):
        if not node_val_list: return 1
        if len(node_val_list) == 1: return 1
        len_node_val_list = len(node_val_list)
        if len_node_val_list in self.dict_num_tree:
            return self.dict_num_tree[len_node_val_list]
        tot_subtree = 0
        for node_val in node_val_list:
            left_list = [node_val_temp for node_val_temp in node_val_list if node_val_temp<node_val]
            len_left_list = len(left_list)
            right_list = [node_val_temp for node_val_temp in node_val_list if node_val_temp>node_val]
            len_right_list = len(right_list)
            if len_left_list in self.dict_num_tree:
                num_left_subtree = self.dict_num_tree[len_left_list]
            else:
                num_left_subtree = self.find_bst(left_list)
                self.dict_num_tree[len_left_list] = num_left_subtree
            if len(right_list) in self.dict_num_tree:
                num_right_subtree = self.dict_num_tree[len(right_list)]
            else:
                num_right_subtree = self.find_bst(right_list)
                self.dict_num_tree[len_right_list] = num_right_subtree
            tot_subtree += num_left_subtree * num_right_subtree
        self.dict_num_tree[len(node_val_list)] = tot_subtree
        return tot_subtree
Solution1 = Solution()
print Solution1.numTrees(3)
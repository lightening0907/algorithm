# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        cur_list = [root]
        val_list = [str(root.val)]
        while len(cur_list):
            pointer = cur_list.pop(0)
            if pointer.left:
                cur_list.append(pointer.left)
                val_list.append(str(pointer.left.val))
            else:
                val_list.append('NA')
            if pointer.right:
                cur_list.append(pointer.right)
                val_list.append(str(pointer.right.val))
            else:
                val_list.append('NA')
        return '_'.join(val_list)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data =='':
            return None
        data_list = data.split('_')


        def _construct_tree(val):
            if val == 'NA':
                return None
            else:
                node = TreeNode(int(val))
            return node
        root = _construct_tree(data_list.pop(0))
        curr_level = [root]


        while len(data_list) > 0:
            next_level = []
            while len(curr_level) > 0 :
                cur_pointer = curr_level.pop(0)
                if cur_pointer:
                    cur_pointer.left = _construct_tree(data_list.pop(0))
                    cur_pointer.right = _construct_tree(data_list.pop(0))
                    next_level.append(cur_pointer.left)
                    next_level.append(cur_pointer.right)
            curr_level = next_level

        return root
#
# class Codec:
#
#     def serialize(self, root):
#         """Encodes a tree to a single string.
#
#         :type root: TreeNode
#         :rtype: str
#         """
#
#         cur_list = [root] #store tree nodes
#         # next_list = [] #store tree nodes
#         val_list = [] #store tree values
#         # store the node value pre order
#         while len(cur_list) >0:
#             pointer = cur_list.pop()
#             while pointer:
#                 val_list.append(str(pointer.val))
#                 cur_list.append(pointer)
#                 pointer = pointer.left
#                 if pointer.right:
#                     cur_list.append(pointer.right)
#         pre_order_str = '_'.join(val_list)
#
#         cur_list = [root] #store tree nodes
#         val_list = [] #store tree values
#
#         # store the node value in order
#         while len(cur_list) > 0:
#             if cur_list[-1].left:
#                 cur_list.append(cur_list[-1].left)
#             else:
#                 pointer = cur_list.pop()
#                 val_list.append(str(pointer.val))
#                 if pointer.right:
#                     cur_list.append(pointer.right)
#         in_order_str = '_'.join(val_list)
#         return pre_order_str + '|' + in_order_str
#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
#
#         :type data: str
#         :rtype: TreeNode
#         """
#         len_data = len(data)
#         pre_order_list = [int(i) for i in data[0:(len_data-1)/2 - 1].split('_')]
#         in_order_list = [int(i) for i in data[(len_data-1)/2 + 1:].split('_')]
#         def _find_root(po_list, io_list): # given preorder list and in order list, return the root node
#             root_val = po_list[0]
#             for i in range(len(io_list)):
#                 if



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
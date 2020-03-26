"""
449. Serialize and Deserialize BST
https://leetcode.com/problems/serialize-and-deserialize-bst/
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""


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
        in_order_str_list = []
        pointer_list = []
        pointer = root
        while pointer:
            in_order_str_list.append(str(pointer.val))
            if pointer.right:
                pointer_list.append(pointer.right)
            if pointer.left:
                pointer = pointer.left
            elif len(pointer_list) > 0:
                pointer = pointer_list.pop()
            else:
                pointer = None
        return ' '.join(in_order_str_list)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) ==0:
            return None
        data_list = [int(tmp) for tmp in data.split(' ')]
        root = self.construct_tree(data_list)
        return root

    def construct_tree(self, data_list):
        len_data_list = len(data_list)
        if len_data_list == 0:
            return None
        root = TreeNode(data_list[0])
        if len_data_list >1:
            r_start = None
            for i in range(0, len_data_list):
                if data_list[i] > data_list[0]:
                    r_start = i
                    break
            if r_start is None:
                root.left = self.construct_tree(data_list[1:len_data_list])
            else:
                if r_start > 1:
                        root.left = self.construct_tree(data_list[1:r_start])
                root.right = self.construct_tree(data_list[r_start:])
        return root

codec = Codec()
root = TreeNode(2)
root.left = TreeNode(1)
# root.right = TreeNode(3)

string = codec.serialize(root)
print(string)
codec.deserialize(string)
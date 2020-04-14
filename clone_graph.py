
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        dict_map = {} # value: old_node, new_node
        dfs = [] # list of nodes to be visited
        dfs_new = [] # list of new nodes to be visited
        if node is not None:
            new_first_node = Node(node.val, [])
            dict_map[node.val] = new_first_node
        else:
            new_first_node = None
        new_pointer = new_first_node
        pointer = node # pointer and new_pointer should point to the same copies

        while pointer:
            for neighbor in pointer.neighbors:
                if neighbor.val not in dict_map:
                    dfs.append(neighbor)
                    new_neighbor = Node(neighbor.val, [])
                    new_pointer.neighbors.append(new_neighbor)
                    dfs_new.append(new_neighbor)
                    dict_map[neighbor.val] = new_neighbor
                elif neighbor.val in dict_map:
                    new_neighbor = dict_map[neighbor.val]
                    new_pointer.neighbors.append(new_neighbor)
            if len(dfs) > 0:
                pointer = dfs.pop()
                new_pointer = dfs_new.pop()
            else:
                pointer = None
                new_pointer = None
        return new_first_node

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors = [node2]
node2.neighbors = [node1]
# node1.neighbors = [node2, node4]
# node2.neighbors = [node1, node3]
# node3.neighbors = [node2, node4]
# node4.neighbors = [node1, node3]

solution = Solution()
solution.cloneGraph(node1)


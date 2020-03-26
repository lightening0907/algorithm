__author__ = 'ChiYuan'
#Definition of TreeNode:
class treenode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

import copy
class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here

        s_path=[]
        marked = {}
        s_path.append(root)

        A_path = []
        B_path = []
        while len(A_path)==0 or len(B_path)==0:

            if (not A_path) and s_path[-1]==A:
                #A_path = copy.copy(s_path)
                #print("hello")
                lA = len(s_path)
                if lA>1:
                    for i in range(lA-1):
                        if s_path[i] in marked:
                            A_path.append(s_path[i])

                            print("A: "+ str(s_path[i].val))
                A_path.append(s_path[-1])

            if (not B_path) and s_path[-1]==B:
                #A_path = copy.copy(s_path)
                lB = len(s_path)
                if lB>1:
                    for i in range(lB-1):
                        if s_path[i] in marked:
                            B_path.append(s_path[i])
                            print("B: " + str(s_path[i].val))
                B_path.append(s_path[-1])
            if s_path[-1] not in marked:
                marked[s_path[-1]] = 1
                if not (s_path[-1].left or s_path[-1].right):
                    del s_path[-1]
                else:
                    ls = len(s_path)
                    if s_path[ls-1].left:
                        s_path.append(s_path[ls-1].left)


                    if s_path[ls-1].right:
                        s_path.append(s_path[ls-1].right)



            else: del s_path[-1]

        l_anc = min(len(A_path),len(B_path))

        print ("l_anc"+str(l_anc))
        for i in range(l_anc):
            if A_path[i]!=B_path[i]:
                print(A_path[i-1].val)
                return A_path[i-1]
            if A_path[l_anc-1]==B_path[l_anc-1]:
                print(A_path[l_anc-1].val)
                return A_path[l_anc-1]

class Solution2(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if (not root) or (p == root) or (q == root) :
            return root
        DFS_list = [(root, 0)]
        ancester_map = {} # map a node to ancester

        goal = {p: None, q:None}
        while len(DFS_list) > 0 and len(goal)>0:
            node, level = DFS_list.pop()
            if node.left:
                DFS_list.append((node.left, level + 1))
                ancester_map[node.left] = (node, level)
                if node.left in goal:
                    del goal[node.left]

            if node.right:
                DFS_list.append((node.right, level + 1))
                ancester_map[node.right] = (node, level)
                if node.right in goal:
                    del goal[node.right]

        ancester_p = (p, ancester_map[p][1] + 1)
        ancester_q = (q, ancester_map[q][1] + 1)
        while ancester_p != ancester_q:
            if ancester_p[1] > ancester_q[1]:
                ancester_p = ancester_map[ancester_p[0]]
            elif ancester_p[1] < ancester_q[1]:
                ancester_q = ancester_map[ancester_q[0]]
            else:
                # if ancester_q == ancester_p:
                #     return ancester_q[0]
                # else:
                ancester_p = ancester_map[ancester_p[0]]
                ancester_q = ancester_map[ancester_q[0]]
        return ancester_q[0]


class Solution3(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #use dfs to find p or q first


        def find_path(node):
            pointer = root
            path = [root]
            dfs = [root]
            while len(path) > 0:


                non_flag = False
                if pointer is None:
                    pointer = dfs[-1]
                    non_flag =True
                if not non_flag and pointer == node:
                    break
                elif not non_flag and pointer.left:
                    dfs.append(pointer.left)
                    path.append(pointer.left)
                    pointer = pointer.left
                elif pointer.right:
                    path.append(pointer.right)
                    dfs.pop()
                    dfs.append(None)
                    dfs.append(pointer.right)
                    pointer = pointer.right
                else:
                    path.pop()
                    dfs.pop()
                    pointer =None
                while len(dfs)>1 and dfs[-1] is None:
                    dfs.pop()
                    path.pop()
            return path

        q_path = find_path(q)
        p_path = find_path(p)

        min_length = min(len(p_path), len(q_path))
        for i in range(min_length):
            if p_path[i] != q_path[i]:
                return p_path[i-1]

        return p_path[i]
tr = treenode(5)
tr2 = treenode(7)
tr3 = treenode(8)
tr4 = treenode(1)
tr5 = treenode(10)
tr6 = treenode(2)
tr7 = treenode(3)
tr.left = tr2
tr.right = tr3
tr2.left =tr4
tr3.right = tr5
tr2.right = tr6
tr3.left = tr7

# tr = treenode(2)
# tr2 = treenode(1)
# tr.right = tr2

print("result:" + str(Solution3().lowestCommonAncestor(tr,tr2,tr3)))
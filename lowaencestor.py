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

print("result:" + str(Solution().lowestCommonAncestor(tr,tr2,tr3).val))
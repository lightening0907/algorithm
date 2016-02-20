__author__ = 'ChiYuan'
class treenode:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

def treeprint(root):
    q_par = []
    q_par.append(root)
    q_child = []
    order = 1
    while len(q_par)>0:
        while len(q_par)>0:
            if order == 1:
                if q_par[-1].left: q_child.append(q_par[-1].left)
                if q_par[-1].right: q_child.append(q_par[-1].right)

                print(q_par[-1].value,end="")
                del q_par[-1]
            else:
                if q_par[-1].right: q_child.append(q_par[-1].right)
                if q_par[-1].left: q_child.append(q_par[-1].left)


                print(q_par[-1].value,end="")
                del q_par[-1]

        print("\n")
        order *= -1
        q_par, q_child = q_child, q_par




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
treeprint(tr)


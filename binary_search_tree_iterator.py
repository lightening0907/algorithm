# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.visited = {}

        self.sorted = []
        if root is not None:
            self.dfs = [root]
        else:
            self.dfs =[]

        while len(self.dfs) > 0:
            pointer = self.dfs[-1]
            if pointer.val not in self.visited:
                self.visited[pointer.val] =True
                if pointer.right:
                    self.dfs.append(pointer.right)
            else:
                ele = self.dfs.pop()
                self.sorted.append(ele.val)
                if ele.left:
                    self.dfs.append(ele.left)



    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        next_ele = self.sorted.pop(0)
        return next_ele


    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if len(self.sorted):
            return True
        return False

class BSTIterator2(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.visited = {}

        # self.sorted = []
        if root is not None:
            self.dfs = [root]
            pointer = self.dfs[-1]
        else:
            self.dfs =[]
            pointer = None

        while pointer is not None:
            self.visited[pointer.val] =True
            if pointer.left:
                self.dfs.append(pointer.left)
            pointer = pointer.left




    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if self.dfs[-1].val in self.visited:
            ele = self.dfs.pop()
            pointer = ele.right
            while pointer:
                self.visited[pointer.val] = True
                self.dfs.append(pointer)
                pointer = pointer.left

        return ele.val


    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if len(self.dfs):
            return True
        return False
tn1 = TreeNode(7)
tn2 = TreeNode(3)
tn3 = TreeNode(15)
tn4 = TreeNode(9)
tn5 = TreeNode(20)
tn1.left = tn2
tn1.right = tn3
tn3.left = tn4
tn3.right = tn5
bstiterator = BSTIterator(tn1)
action = ["next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]
for a in action:
    if a == 'next':
        print(bstiterator.next())
    else:
        print(bstiterator.hasNext())
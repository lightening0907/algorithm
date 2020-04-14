"""
341. Flatten Nested List Iterator
https://leetcode.com/problems/flatten-nested-list-iterator/
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false,
             the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false,
             the order of elements returned by next should be: [1,4,6].
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nestedList = nestedList
        self.DFS = []



    def next(self):
        """
        :rtype: int
        """
        while len(self.DFS) >0 or len(self.nestedList)>0:
            if len(self.DFS) == 0:
                nested_integer = self.nestedList.pop(0)

            else:
                nested_integer = self.DFS.pop(0)
                if isinstance(nested_integer, int):
                    return nested_integer
            while not nested_integer.isInteger():
                nestedList = nested_integer.getList()
                if len(nestedList) ==0:
                    break
                nested_integer = nestedList[0]
                if len(nestedList) > 1:
                    self.DFS = nestedList[1:] + self.DFS
            if nested_integer.isInteger():
                return nested_integer.getInteger()




    def hasNext(self):
        """
        :rtype: bool
        """
        next_ele = self.next()
        if next_ele is not None:
            self.DFS.insert(0, next_ele)
            return True
        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
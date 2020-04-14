# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
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

class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        curr_candidate = nestedList
        sum_by_level = []
        while len(curr_candidate) > 0:
            next_candidate = []
            sum_by_level.append(0)
            print(sum_by_level)
            while len(curr_candidate) > 0:
                candidate = curr_candidate.pop()
                if candidate.isInteger():
                    # print(1)
                    sum_by_level[-1] += candidate.getInteger()
                else:
                    # print(2)
                    next_candidate.extend(candidate.getList())
            curr_candidate = next_candidate
        depth = len(sum_by_level)
        total_sum = 0
        # print(sum_by_level)
        for ele in sum_by_level:
            total_sum += ele * depth
            depth -= 1
        # print(total_sum)
        return total_sum
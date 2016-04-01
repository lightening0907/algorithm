"""Given two integers n and k, return all possible combinations of k numbers out of 1 ... n."""


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # self.combine = []
        self.listnum = range(1, n + 1)
        if n == k:
            return [self.listnum]
        else:
            sublist1 = self.find(1, n - 1, k - 1, 1)  # use recursive method, given find one value, find k-1 value in the rest of numbers
            sublist2 = self.find(1, n - 1, k, None)
        return sublist1 + sublist2

    def find(self, i, end, k, val): # val indicate whether there is a value waiting to be combine into the k-item set found in this function
        if k == 0:
            sublist = [[]]
        elif end - i + 1 == k:
            return [self.listnum[i:]]
        elif end - i + 1 > k:
            sublist1 = self.find(i + 1, end, k - 1, self.listnum[i])
            sublist2 = self.find(i + 1, end, k, None)
            sublist = sublist1 + sublist2
        if val:
            for value in sublist:
                value.insert(0, val)
        return sublist


Solution1 = Solution()
print Solution1.combine(2, 1)

# the method of keep finding the next permutation sequence is two slow
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        f_sq = range(1,n+1) # first sequence
        nums = f_sq
        for i in range(k-1):
            self.nextPermutation(nums,n)
        return ''.join(str(x) for x in nums)

    def nextPermutation(self,nums,n):
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                min_max = nums[i + 1]
                min_max_index = i + 1
                for j in range(i+1,n):
                    if nums[j]>nums[i]:
                        min_max = nums[j]
                        min_max_index = j
                    else:
                        break
                nums[i],nums[min_max_index] = nums[min_max_index], nums[i]
                nums[i+1:]=nums[n-1:i:-1]
                return

from math import factorial

"""
find which buckets contains the kth sequence
each sequence start with i contains (n-1)! sequences respectively
then the first digit is j if kth > (j-1)(n-1)!
similary the second digit is the j'th digit in the remaining sequence (1,2,3..n) after excluding j
if kth-(j-1)(n-1)! > (j'-1)(n-2)!
"""
class Solution2(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        kth_num = ""
        list_num = range(1,n+1)
        while n>0:
            num,rest = divmod((k-1),factorial(n - 1))
            k = rest + 1
            n -= 1
            kth_num += str(list_num[num])
            del list_num[num]
        return kth_num

Solution1 = Solution()
print Solution1.getPermutation(8,38790)
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        len_nums = len(nums)
        if len_nums == 0:
            return False
        dp = nums[:-1]
        for i in range(1, len_nums):
            for j in range(i):
                dp[j] = dp[j] + nums[i]
                if dp[j]==k or (k!=0 and dp[j]%k == 0):
                    return True
        return False

Solution1 = Solution()
print(Solution1.checkSubarraySum([0,0], 0))
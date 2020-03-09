"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        min_num = max(1, min(nums))
        nums =  [ele - min_num for ele in nums]
        len_nums = len(nums)
        for i in range(len_nums):
            while nums[i] >= 0 and nums[i] != i and nums[i] < len_nums:
                index_tmp = nums[i]
                nums[i], nums[index_tmp] = nums[index_tmp], nums[i]
        for i in range(len_nums):
            if nums[i] != i:
                if i == 0:
                    return 1
                return nums[i-1] + min_num +1
        if min_num == 1:
            return max(nums) + 1
        else:
            return min_num - 1

print Solution().firstMissingPositive([3, 4, -1, 1])
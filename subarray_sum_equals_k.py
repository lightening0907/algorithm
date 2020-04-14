"""
560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        candidate_sum = []
        num_subarray = 0
        len_nums = len(nums)
        for num_index, num in enumerate(nums):
            for cand_index in range(len(candidate_sum)):
                candidate_sum[cand_index] += num
                if candidate_sum[cand_index] == k:
                    num_subarray += 1
            if num == k:
                num_subarray += 1
            candidate_sum.append(num)
        return num_subarray

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        candidate_sum = []
        num_subarray = 0
        len_nums = len(nums)
        accum_sum = []
        num_res = 0
        for index_num, num in enumerate(nums):
            if index_num == 0 :
                accum_sum.append(num)
            else:
                accum_sum.append(num + accum_sum[-1])
        print accum_sum
        for start in range(len_nums):
            for end in range(start, len_nums):
                if start > 0:
                    if accum_sum[end] - accum_sum[start-1] == k:
                        num_res += 1
                else:
                    if accum_sum[end] == k:
                        num_res += 1
        return num_res

solution = Solution()
print(solution.subarraySum([1, 1, 1], 2))
"""
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
Note:
The pairs (i, j) and (j, i) count as the same pair.
The length of the array won't exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].
"""

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        len_nums = len(nums)
        # k = abs(k)
        if len_nums == 1:
            return 0
        num_pairs = 0
        l_index = 0
        r_index = 1
        old_diff = None
        while r_index < len_nums:
            new_diff = nums[r_index] - nums[l_index]
            if l_index == r_index:
                r_index += 1
            elif old_diff == k and (nums[r_index] == nums[r_index - 1]) and (nums[l_index] == nums[l_index - 1]):
                r_index += 1
                l_index += 1
            elif new_diff == k:
                num_pairs += 1
                r_index += 1
                l_index += 1
            elif new_diff > k:
                l_index += 1
            elif new_diff < k:
                r_index += 1
            old_diff = new_diff
        return num_pairs

print Solution().findPairs([3,1,4,1,5], 2)

"""
398. Random Pick Index
https://leetcode.com/problems/random-pick-index/
Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
"""
from random import randint
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums


    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        num_target = 0
        sample_index = None
        for num_index, num in enumerate(self.nums):
            if num == target:
                num_target += 1
                if sample_index is None:
                    sample_index = num_index
                else:
                    rand_int = randint(1, num_target)
                    if rand_int == 1:
                        sample_index = num_index
        return sample_index

"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """


        len_nums = len(nums)
        if len_nums<2: return
        for i in range(len_nums-2,-1,-1):
            # find the first element where the i+1th > ith, which is the first time number start to decrease from right to left
            if nums[i]<nums[i+1]:
                min_max_i = nums[i+1]
                min_max_index = i+1
                for j in range(i+1,len_nums):
                    # find the smallest element on the right of i but larger than nums[i] to swap with it
                    if nums[j]>nums[i] and nums[j]<min_max_i:
                        min_max_i = nums[j]
                        min_max_index = j
                    if nums[j]<nums[i]: break
                nums[i],nums[min_max_index]=nums[min_max_index],nums[i]
                # the right hand site of i will need to be in decreasing order
                nums[i+1:] = sorted(nums[i+1:])
                return
        nums.sort()

Solution1 = Solution()
nums = [1,3,2]
Solution1.nextPermutation(nums)
print nums
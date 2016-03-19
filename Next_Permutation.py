class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """


        len_nums = len(nums)
        if len_nums<2: return
        for i in range(len_nums-2,-1,-1):
            if nums[i]<nums[i+1]:
                min_max_i = nums[i+1]
                min_max_index = i+1
                for j in range(i+1,len_nums):
                    if nums[j]>nums[i] and nums[j]<min_max_i:
                        min_max_i = nums[j]
                        min_max_index = j
                    if nums[j]<nums[i]: break
                nums[i],nums[min_max_index]=nums[min_max_index],nums[i]
                nums[i+1:] = sorted(nums[i+1:])
                return
        nums.sort()

Solution1 = Solution()
nums = [1,3,2]
Solution1.nextPermutation(nums)
print nums
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        first_zero_pos = -1
        last_zero_pos = -1
        for i in range(len(nums)):
            if nums[i] ==0  and first_zero_pos == -1:
                first_zero_pos = i
                last_zero_pos = i
            # elif nums[i] ==0  and i < first_zero_pos:
            #     first_zero_pos = i
            elif nums[i] !=0 and first_zero_pos!=-1:
                nums[first_zero_pos], nums[i] = nums[i], nums[first_zero_pos]
                first_zero_pos = first_zero_pos + 1
                last_zero_pos = i
        return nums

Solution1=Solution()
print(Solution1.moveZeroes([1,0, 1]))
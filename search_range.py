"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums
        self.target = target
        if not nums: return [-1,-1]
        if target < nums[0] or target > nums[-1]: return [-1,-1]
        self.len_nums = len(nums)
        res_range = [-1,-1]
        left = 0
        right = self.len_nums - 1
        if nums[left] == target and nums[right] == target:
            return [left,right]
        if nums[left] == target:
            res_range[0] = left
        else: res_range[0] = self.searchRange_Left(left,right)
        if nums[right] == target:
            res_range[1] = right
        else: res_range[1] = self.searchRange_Right(left,right)
        return res_range
    def searchRange_Left(self,left,right):
        if self.nums[left] == self.target: return left
        if left == right and self.nums[left] != self.target:
            return -1
        if left == right - 1:
            if self.nums[right] != self.target:
                return -1
            else:
                return right
        mid = (left + right)//2
        if self.nums[mid] < self.target: return self.searchRange_Left(mid,right)
        if self.nums[mid] == self.target and (mid == 0 or self.nums[mid-1] != self.target):
            return mid
        else:
            return self.searchRange_Left(left,mid-1)
    def searchRange_Right(self,left,right):
        if self.nums[right] == self.target: return right
        if left == right and self.nums[left] != self.target:
            return -1
        if left == right - 1:
            if self.nums[left] != self.target:
                return -1
            else: return left
        mid = (left + right)//2
        if self.nums[mid] < self.target: return self.searchRange_Right(mid,right)
        if self.nums[mid] == self.target and (mid ==self.len_nums-1 or self.nums[mid+1] != self.target):
            return mid
        if self.nums[mid] == self.target:
            return self.searchRange_Right(mid+1,right)
        if self.nums[mid] > self.target:
            return self.searchRange_Right(left,mid-1)

Solution1 = Solution()
print Solution1.searchRange([1,2,3],1)


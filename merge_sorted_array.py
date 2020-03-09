"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        if n >0:
            nums1_index = 0
            nums2_index = 0
            tot_nums1 = m
            while nums2_index < n and nums1_index < m + n:
                if nums1_index == tot_nums1:
                    nums1[nums1_index: n - nums2_index + nums1_index] = nums2[nums2_index:n]
                    break
                if nums1_index == 0 and nums2[nums2_index] < nums1[0]:
                    nums1[1:tot_nums1+1] = nums1[0:tot_nums1]
                    nums1[0] = nums2[nums2_index]
                    tot_nums1 += 1
                    nums1_index += 1
                    nums2_index += 1
                elif nums2[nums2_index] > nums1[nums1_index]:
                    nums1_index += 1
                elif nums2[nums2_index] <= nums1[nums1_index]:
                    nums1[nums1_index + 1:tot_nums1+1] = nums1[nums1_index:tot_nums1]
                    nums1[nums1_index] = nums2[nums2_index]
                    nums1_index += 1
                    nums2_index += 1
                    tot_nums1 += 1
            print nums1

print Solution().merge([0], 0, [1], 1)
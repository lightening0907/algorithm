class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len_num1 = len(nums1)
        len_num2 = len(nums2)
        if len_num1+len_num2 & 1:
            return self.findKth((len_num1+len_num2)//2,nums1,nums2)
        else:

            m1 = self.findKth((len_num1+len_num2)//2,nums1,nums2)
            m2 = self.findKth((len_num1+len_num2-1)//2,nums1,nums2)
            return (m1 + m2)/2

    def findKth(self,k,nums1,nums2):
        len_num1 = len(nums1)
        len_num2 = len(nums2)
        mid1 = len_num1//2
        mid2 = len_num2//2
        if not nums1 and not nums2: return None
        if not nums1: return float(nums2[k])
        if not nums2: return float(nums1[k])
        if nums1[mid1] >= nums2[mid2]:
            # left = len_num1//2 + len_nums2//2
            # right = len_num1 + len_num2 - left
            if len_num2//2 >= k:
                return self.findKth(k,nums1[:len_num1//2],nums2[:len_num2//2+1])
            else:
                if len_num2 >1:
                    return self.findKth(k-len_num2//2,nums1,nums2[len_num2//2:])
                elif len_num2 == 1 and 1 + len_num1//2>k:
                    return self.findKth(k,nums1[:len_num1//2],nums2)
                else:
                    return float(nums1[k-len_num2//2-1])

        else:
            if len_num1//2 >= k:
                return self.findKth(k,nums1[:len_num1//2+1],nums2[:len_num2//2])
            else:
                if len_num1>1:
                    return self.findKth(k - len_num1//2,nums1[len_num1//2:],nums2)
                if len_num1 == 1 and 1 + len_num2//2 > k:
                    return self.findKth(k,nums1,nums2[:len_num2//2])
                else:
                    return float(nums2[k - len_num1//2 -1])

Solution1 = Solution()
print Solution1.findMedianSortedArrays([1,1,3,3],[1,1,3,3])
"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        len_nums = len(nums)
        dict1 = {}
        dict2 = {}
        result_l = []
        if len_nums<3: return result_l
        nums.sort()
        for i in range(len_nums):
            if nums[i] in dict2: # dict2 is the dictionary where key is the candidate num that adds up to 0 with its values (list of list)
                for temp_l in dict2[nums[i]]:
                    temp_l2 = (temp_l + [nums[i]])
                    if temp_l2 not in result_l:
                        result_l.append(temp_l2)
            if i<len_nums-1:
                if dict1 and nums[i] not in dict1: # dict1 is the dictionary where key is the value already appeared in the list, and value is the frequency it had appeared
                    for k_dict1 in dict1: # if nums[i] is a new number, make combination of every key in dict1 to form values in dict2
                        rest = -k_dict1-nums[i]
                        if rest not in dict2:
                            dict2[rest] = [[k_dict1,nums[i]]]
                        else:
                            dict2[rest].append([k_dict1,nums[i]])
                elif dict1.setdefault(nums[i],0)==1: # if nums[i] already occurred once (and only once), then only add it with itself to form candidate in dict2
                    rest = -2*nums[i]
                    if rest not in dict2:
                        dict2[rest] = [[nums[i],nums[i]]]
                    else:
                        dict2[rest].append([nums[i],nums[i]])
            dict1[nums[i]] = dict1.setdefault(nums[i],0) + 1
        return


Solution1=Solution()
print Solution1.threeSum([1,2,-2,-1])


class Solution2(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        len_nums = len(nums)
        nums = sorted(nums)
        solution = []
        if len_nums < 3:
            return False
        for i in range(0, len_nums):
            for j in range(i + 1, len_nums):
                for k in range(j+1, len_nums):
                    if nums[i] + nums[j] + nums[k] > 0:
                        break
                    if nums[i] + nums[j] + nums[k]  == 0:
                        solution.append([nums[i], nums[j], nums[k]])
        return solution

class Solution3(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        len_nums = len(nums)
        nums = sorted(nums)
        solution = []
        if len_nums < 3:
            return []
        for i in range(0, len_nums):
            j, k = i + 1, len_nums -1
            while j < k:
                if nums[j] + nums[k] + nums[i] < 0:
                    j += 1
                elif nums[j] + nums[k] + nums[i] > 0:
                    k -= 1
                elif i > 0 and nums[i] == nums[i-1]:
                    break
                elif (j > i + 1 and nums[j] == nums[j -1]):
                    j += 1
                elif (k < len_nums - 1 and nums[k] == nums[k + 1]):
                    k -= 1
                else:
                    solution.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1


        return solution
solution = Solution3()
print(solution.threeSum([-1,0,1,2,-1,-4]))
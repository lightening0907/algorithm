"""
698. Partition to K Equal Sum Subsets
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.



Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.


Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
"""
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # use dp to save all the potential candidate
        # cadidate has the structure dictionary list of list of cum_sum for the nth number
        nums = sorted(nums)
        print nums
        total = sum(nums)

        if total % k != 0:
            return False # false if can't divide equally
        else:
            equal_size = total // k
        print(total, equal_size)
        len_nums = len(nums)
        candidate = []
        for num_index in range(len_nums):
            if num_index ==0:
                candidate.append([nums[0]])
                continue
            else:
                len_candidate = len(candidate)
                new_candidate = []
                for candidate_index in range(len_candidate):
                    len_ele = len(candidate[candidate_index])
                    # if candidate[candidate_index] == [20, 13, 13]:
                        # print(num_index, candidate_index)
                    add_ele_flag = True

                    break_flag = False
                    for ele_index in range(len_ele):
                        if candidate[candidate_index][ele_index] + nums[num_index] > equal_size:
                            break_flag = True
                            break
                    if break_flag:
                        continue

                    for ele_index in range(len_ele):
                        if candidate[candidate_index][ele_index] + nums[num_index] == equal_size:
                            # print(num_index, candidate[candidate_index])
                            if num_index == len_nums - 1 and len_ele == 1:
                                print(candidate)
                                return True
                            if len_ele == 1:
                                new_candidate.append([0])
                            else:
                                if ele_index < len_ele -1:
                                    new_candidate.append(candidate[candidate_index][:ele_index] + candidate[candidate_index][ele_index+1:])
                                else:
                                    new_candidate.append(candidate[candidate_index][:ele_index])
                        elif candidate[candidate_index][ele_index] + nums[num_index] < equal_size:
                            if ele_index < len_ele -1:
                                # print candidate[candidate_index][:ele_index] + [candidate[candidate_index][ele_index] + nums[num_index]] + candidate[candidate_index][ele_index+1:]
                                new_candidate.append(candidate[candidate_index][:ele_index] + [candidate[candidate_index][ele_index] + nums[num_index]] + candidate[candidate_index][ele_index+1:])
                            else:
                                # print candidate[candidate_index][:ele_index] +[candidate[candidate_index][ele_index] + nums[num_index]]
                                new_candidate.append(candidate[candidate_index][:ele_index] + [candidate[candidate_index][ele_index] + nums[num_index]])
                        else:
                            add_ele_flag= False
                            break

                    if add_ele_flag and len_ele < k:
                        new_candidate.append(candidate[candidate_index] + [nums[num_index]])
            candidate = new_candidate
        return False


solution = Solution()
print(solution.canPartitionKSubsets([114,96,18,190,207,111,73,471,99,20,1037,700,295,101,39,649], 4))
#print(solution.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))


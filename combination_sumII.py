"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        combination_sets = []
        len_candidates = len(candidates)
        if len_candidates == 0:
            return []
        for index_c in range(len_candidates):
            if candidates[index_c] < target and (index_c == 0 or candidates[index_c] != candidates[index_c-1]) :
                combination_sets_tmp = self.combinationSum2(candidates[index_c+1:], target-candidates[index_c])
                if len(combination_sets_tmp) > 0:
                    for combination_set_tmp in combination_sets_tmp:
                        combination_sets.append([candidates[index_c]] + combination_set_tmp[:])
            elif candidates[index_c] == target:
                combination_sets.append([candidates[index_c]])
                break
        return combination_sets

print Solution().combinationSum2([2,5,2,1,2], 5)
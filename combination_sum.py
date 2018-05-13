"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.dict_combine = {}
        self.candidates = candidates
        self.candidates.sort()
        list_combine = []
        self.len_c = len(self.candidates)
        list_combine = self.recur_comb(0,target)
        return list_combine

    def recur_comb(self,index,target):
        if index>=self.len_c: return []
        temp_list_combine = []
        if (index,target) in self.dict_combine:
            return dict_combine[(index,target)]

        temp_element = self.candidates[index]
        temp_list = []
        freq = 0
        if temp_element > target: return []
        while temp_element*freq <= target:
            temp_list = [temp_element]*freq
            if temp_element*freq == target:
                temp_list_combine.append(temp_list)
                if (index,target) not in self.dict_combine:
                    self.dict_combine[(index,target)]=[]
                self.dict_combine[(index,target)].append(temp_list)
                print target,temp_list
                break
            if (index+1,target-temp_element*freq) in self.dict_combine:
                rest = self.dict_combine[(index+1,target-temp_element*freq)]
                # continue
            else:
                rest = self.recur_comb(index+1,target-temp_element*freq)
            if rest and (index,target) not in self.dict_combine:
                self.dict_combine[(index,target)] = []
            for item in rest:
                temp_list_combine.append(temp_list + item)
                print target,temp_list + item
                self.dict_combine[(index,target)].append(temp_list + item)
            freq +=1

        return temp_list_combine

Solution1 = Solution()
print Solution1.combinationSum([4,2,7,5,6],16)
#[1,2,5],7
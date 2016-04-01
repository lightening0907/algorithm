class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums: return False
        len_nums = len(nums)
        index = 0
        current_index_list = [0]
        while current_index_list:
            next_index_list = []
            for current_index in current_index_list:
                if current_index == len_nums -1: return True
                elif nums[current_index] == 0:
                    # del nums[current_index]
                    continue
                for jump in range(nums[current_index]+1,0,-1):
                    next_index = current_index + jump
                    if next_index == len_nums-1: return True
                    if next_index < len_nums-1 and next_index not in next_index_list:
                        next_index_list.append(next_index)
            current_index_list = next_index_list
        return False

class Solution2(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums: return False
        len_nums = len(nums)
        index = 0
        current_index_list = [0]
        # jumped_dict = []
        while current_index_list:
            if current_index_list[-1] > len_nums -1 or nums[current_index_list[-1]] == 0:
                del current_index_list[-1]
                continue
            if current_index_list[-1] == len_nums -1: return True

            temp_index = current_index_list[-1]
            del current_index_list[-1]
            current_index_list += range(1+temp_index,temp_index + nums[temp_index]+1)

        return False
Solution1 = Solution2()
print Solution1.canJump([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
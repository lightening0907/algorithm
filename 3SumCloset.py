class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sorted_nums = sorted(nums)
        len_nums = len(sorted_nums)
        first_index, second_index, third_index = 0, 1, len_nums-1
        closet_sum = None
        while first_index <= len_nums -3:
            while second_index < third_index:
                if closet_sum is None:
                    closet_sum_temp = sorted_nums[first_index] + sorted_nums[second_index] \
                                     + sorted_nums[third_index]
                    closet_sum = closet_sum_temp

                else:
                    closet_sum_temp = sorted_nums[first_index] + sorted_nums[second_index] \
                                     + sorted_nums[third_index]
                    if abs(closet_sum - target) > abs(closet_sum_temp - target):
                        closet_sum = closet_sum_temp
                if closet_sum_temp == target:
                    return target
                elif closet_sum_temp > target:
                    third_index -= 1
                else:
                    second_index += 1
            first_index += 1
            second_index = first_index + 1
            third_index = len_nums -1
        return closet_sum
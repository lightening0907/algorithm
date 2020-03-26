class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        nums = sorted(nums) #ascending order
        if len_nums <3:
            return 0

        dp = {} # dictionary potential longest edge: number of triangle, save number of triagle that is possible if this number is possible
        tot_sol = 0
        first_edge = []
        second_edge = None
        for i in range(0, len_nums):
            # if second_edge + first_edge[-1] <= nums[i]:
            #     first_edge = first_edge[:] + second_edge[:-second_index+1]
            #     second_edge = second_edge[-second_index+1:]
            #     break
            if len(first_edge)==0 and nums[i]!=0:
                first_edge = [nums[i]] #ascending order
            elif len(first_edge)>0 and not second_edge and nums[i]!=0:
                second_edge = nums[i] #elemet in second edge
            elif len(first_edge)>0 and second_edge:
                for first_index in range(1, len(first_edge)+1):
                    two_edge_sum = second_edge + first_edge[-first_index]
                    if two_edge_sum > nums[i]:
                        for dp_index in range(second_edge + 1, two_edge_sum):
                            if dp_index in dp:
                                dp[dp_index] += 1
                            else:
                                dp[dp_index] = 1
                        if nums[i] == second_edge:
                            if nums[i] in dp:
                                dp[nums[i]] += 1
                            else:
                                dp[nums[i]] = 1
                    else:
                        break
                first_edge.append(second_edge)
                second_edge = nums[i]
                if nums[i] in dp:
                    tot_sol += dp[nums[i]]
        return tot_sol

solution = Solution()
print(solution.triangleNumber([0,1,1,1]))
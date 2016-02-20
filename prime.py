__author__ = 'ChiYuan'
import math
import copy
class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n ==0 or n==1: return 0
        nums = list(range(2,n+1))
        nums2 = copy.copy(nums)
        prime_l = []

        while nums[0]<=math.sqrt(n):
            prime_l.append(nums[0])
            temp_v = nums[0]

            i=0
            while nums[i]*nums[0]<=n:
                nums2.remove(nums[i]*nums[0])
                i += 1
            del nums2[0]
            nums = copy.copy(nums2)
       # print("prime_l")
       # print(prime_l)
       # print('num')
       # print(nums)
        return len(prime_l)+len(nums)


print(Solution().countPrimes(100000))
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


class Solution2(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2: return 0
        if n<=3: return 1
        count = 1
        prime = [2]
        for i in range(3,n):
            # this method is too slow as it needs to check over the same prime numbers again and again
            for div in prime:
                if i%div==0:break
                if div>i**0.5:
                    prime.append(i)
                    count +=1
                    break
        return count

#this method proactively mark off the non-prime number, which are the beishu of prime numbers
class Solution3(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: return 0

        init_ret = [1]*n
        init_ret[0:2]=[0]*2
        prime = 2
        count = n-2
        for i in range(2,n):
            if i>n**0.5: break
            if init_ret[i]==0: continue
            else: prime = i
            # only multiply the prime number with number larger than itself
            j = prime*prime

            while j<n:
                if init_ret[j]==1:
                    init_ret[j]=0 #mark off the number with a prime as divisor
                    count -= 1
                j +=prime
        return count
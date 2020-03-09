from copy import copy
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """

        len_primes = len(primes)
        min_index_list = [0]*len_primes
        ungly_num_candidate = copy(primes)
        ungly_num_list = [1]
        index = 1
        ugly_num = 1
        while index <= n - 1:
            ugly_num = min(ungly_num_candidate)
            ungly_num_list.append(ugly_num)
            # print 'ugly_num', ugly_num
            for prime_index, prime_number in enumerate(primes):
                if ungly_num_list[min_index_list[prime_index]]*prime_number == ugly_num:
                    min_index_list[prime_index] += 1
                    ungly_num_candidate[prime_index] = ungly_num_list[min_index_list[prime_index]] * prime_number
            index += 1
        return ugly_num

Solution1 = Solution()
print Solution1.nthSuperUglyNumber(4, [2])
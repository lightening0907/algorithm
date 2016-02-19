class Solution(object):
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
class Solution2(object):
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
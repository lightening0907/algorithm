import random
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w_len = len(w)
        self.w = w
        self.sum_w = sum(self.w)
        self.cum_w = self.w[:]
        for i in range(len(self.cum_w)):
            if i != 0:
                self.cum_w[i] += self.cum_w[i-1]


    def pickIndex(self):
        """
        :rtype: int
        """
        random_w = random.randint(1, self.sum_w)
        left, right = 0, self.w_len - 1

        while right - left >1:
            mid = (left + right)//2
            if self.cum_w[mid] < random_w:
                left = mid
            elif self.cum_w[mid] > random_w:
                right = mid
            else:
                return mid
        if random_w > self.cum_w[left]:
            return right
        else:
            return left

solution = Solution([3, 14, 1, 17])
for i in range(100):
    print(solution.pickIndex())
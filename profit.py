__author__ = 'ChiYuan'
class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if not prices: return 0
        len_pr = len(prices)
        bs_p = [prices[0],prices[0]] #buy and sell
        bs_pt = [bs_p[0],bs_p[1]]
        for i in range(1,len_pr):
            bs_pt[1] = prices[i]
            if (prices[i]>prices[i-1]) and (prices[i]>bs_p[1]):
                bs_p[1] = prices[i]
            elif (prices[i]<prices[i-1]) and (prices[i]<bs_p[0]):
                bs_pt[0] = prices[i]
            if (bs_pt[1] - bs_pt[0])>(bs_p[1] - bs_p[0]):
                bs_p = [bs_pt[0],bs_pt[1]]
        return (bs_p[1]-bs_p[0])

print(Solution().maxProfit([1,4,2]))
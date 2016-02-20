# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l_p = len(prices)
        if l_p<2: return 0
        t_b = 0
        t_s = 0
        p_b = 0
        #p_s = 0
        for i in range(1,l_p):
            if (prices[i]-prices[p_b])>(prices[t_s]-prices[t_b]):
                t_s = i
                t_b = p_b
                #else: p_s = i
            if prices[i]<prices[p_b]:
                p_b = i
        return prices[t_s]-prices[t_b]

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cur_b = 0
        cur_s = 0
        cur_prof = 0
        cum_prof = 0
        len_p = len(prices)
        for i in range(1,len_p):
            if prices[i]>=prices[i-1]:
                cur_s = i
                cur_prof = prices[cur_s] - prices[cur_b]
            else:
                cum_prof += cur_prof
                cur_b = i
                cur_s = i
                cur_prof = prices[cur_s] - prices[cur_b]
        cum_prof += cur_prof
        return cum_prof
"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        last_level_dict = {amount:0}
        next_level_dict = {}
        level = 1
        last_level_len = True
        while last_level_len:
            last_level_len = False
            for coin in coins:
                for key in last_level_dict:
                    if key - coin > 0:
                        next_level_dict[key-coin] = 0
                        last_level_len = True
                    elif key - coin == 0:
                        return level
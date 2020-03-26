"""
464. Can I Win
https://leetcode.com/problems/can-i-win/

In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

Example

Input:
maxChoosableInteger = 10
desiredTotal = 11

Output:
false

Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
"""

class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if (1 + maxChoosableInteger)*maxChoosableInteger/2 == desiredTotal:
            if maxChoosableInteger % 2 == 0:
                return False
            else:
                return True
        candidate = range(1, maxChoosableInteger+1)
        self.dict_inter = {} # tuple: True / False
        return self._canIWin(candidate, desiredTotal)


    def _canIWin(self, candidate, desiredTotal):
        if tuple(candidate) in self.dict_inter:
            return self.dict_inter[tuple(candidate)]
        res = self.judge(candidate, desiredTotal)
        if res is not None:
            return res
        if res is None:
            candidate_len = len(candidate)
            #opponent = False # assume opponent will not win
            for i in range(candidate_len):
                if i == 0:
                    new_candidate = candidate[1:]
                elif i == candidate_len - 1:
                    new_candidate = candidate[:-1]
                else:
                    new_candidate = candidate[:i] + candidate[i+1:]
                opp_res = self._canIWin(new_candidate, desiredTotal - candidate[i])
                if tuple(new_candidate) not in self.dict_inter:
                    self.dict_inter[tuple(new_candidate)] = opp_res
                if not opp_res:
                    self.dict_inter[tuple(candidate)] = True
                    return True
            self.dict_inter[tuple(candidate)] = False
            return False



    def judge(self,candidate, desiredTotal):
        # print(candidate, desiredTotal)
        if candidate[-1] >= desiredTotal: # a sure winning case
            # can not win this round
            return True
        if candidate[-1] + candidate[0] >= desiredTotal: # a sure losing case
            return False
        return None


solution = Solution()
print(solution.canIWin(20, 209))
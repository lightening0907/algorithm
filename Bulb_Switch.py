"""
There are n bulbs that are initially off.
You first turn on all the bulbs.
Then, you turn off every second bulb.
On the third round, you toggle every third bulb
(turning on if it's off or turning off if it's on).
For the ith round, you toggle every i bulb. For the nth round,
you only toggle the last bulb. Find how many bulbs are on after n rounds.
"""

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_on = 0
        i = 1
        while i<=n:
            if i**2 <= n:
                num_on += 1
                i += 1
            else:
                break
        return num_on
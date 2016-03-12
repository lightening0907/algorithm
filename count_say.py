"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        cnt_say = "1"
        if n == 1: return cnt_say
        for i in range(1,n):
            l_cnt_say = len(cnt_say)
            temp_cnt_say = ""
            cnt = 1
            for ind_cs in range(1,l_cnt_say):
                if cnt_say[ind_cs] != cnt_say[ind_cs-1]:
                    temp_cnt_say += str(cnt) + cnt_say[ind_cs-1]
                    cnt = 1
                else:
                    cnt += 1
            temp_cnt_say += str(cnt) + cnt_say[-1]
            cnt_say = temp_cnt_say
        return cnt_say

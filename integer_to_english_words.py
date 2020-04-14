"""
273. Integer to English Words
https://leetcode.com/problems/integer-to-english-words/
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        location_map = {3: 'Hundred', 4: 'Thousand', 7: 'Million',
                        10: 'Billion'}

        word_map_below_20 = {1: 'One', 2: 'Two', 3:'Three',
                             4: 'Four', 5: 'Five', 6: 'Six',
                             7: 'Seven', 8: 'Eight', 9: 'Nine',
                             10: 'Ten', 11: 'Eleven', 12: 'Twelve',
                             13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
                             16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
                             19: 'Nineteen'}

        word_map_above_20 = {2: 'Twenty', 3:'Thirty', 4:'Forty', 5: 'Fifty', 6: 'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninety'}

        key_intervals = [3, 4, 7, 10]
        size_counter = 0
        res_list = [] # will return in reverse order
        if num == 0:
            return 'Zero'
        k_index_init = 0
        num_stack = []
        while num>0:
            num_next, num_mod = divmod(num, 10)
            size_counter += 1

            for k_index in range(k_index_init, len(key_intervals)):
                if size_counter < key_intervals[k_index] and (k_index ==0 or (k_index > 0 and size_counter - key_intervals[k_index-1]<2)):
                    k_index_init = k_index
                    num_stack.append(num_mod)
                    break
                elif size_counter == key_intervals[k_index] or size_counter - key_intervals[k_index-1]==2:
                    if size_counter == key_intervals[k_index]:
                        k_index_init = k_index + 1
                    tmp_sum = 0
                    while len(num_stack) > 0:
                        tmp_sum = tmp_sum*10 + num_stack.pop()
                    if tmp_sum == 0 and len(res_list) > 0 and (((size_counter - key_intervals[k_index-1]==2) and num_next !=0 and num_mod ==0) \
                        or (num_next !=0 and num_mod ==0 and key_intervals[k_index] - size_counter == 1) \
                        or (key_intervals[k_index] == size_counter)) : #
                        res_list.pop()
                    elif tmp_sum < 20 and tmp_sum > 0:
                        res_list.append(word_map_below_20[tmp_sum])
                    elif tmp_sum >= 20:
                        tmp_sum, tmp_sum_remain = divmod(tmp_sum, 10)
                        if tmp_sum_remain > 0:
                            res_list.append(word_map_below_20[tmp_sum_remain])
                        res_list.append(word_map_above_20[tmp_sum])
                    num_stack = []
                    num_stack.append(num_mod)
                    if size_counter == key_intervals[k_index]:
                        res_list.append(location_map[key_intervals[k_index]])
                    else:
                        res_list.append('Hundred')
                    break

            if size_counter == key_intervals[-1]:

                size_counter = 0
                k_index_init = 0
            num = num_next

        tmp_sum = 0
        while len(num_stack) > 0:
            tmp_sum = tmp_sum*10 + num_stack.pop()

        if tmp_sum < 20 and tmp_sum > 0:
            res_list.append(word_map_below_20[tmp_sum])
        if tmp_sum >= 20:
            tmp_sum, tmp_sum_remain = divmod(tmp_sum, 10)
            if tmp_sum_remain > 0:
                res_list.append(word_map_below_20[tmp_sum_remain])
            res_list.append(word_map_above_20[tmp_sum])

        return ' '.join(reversed(res_list))

solution = Solution()
print(solution.numberToWords(3055000))
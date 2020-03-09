# -*- coding: utf-8 -*-
"""
1.给定数组，求longest consecutive subarray
例如：输入｛1，4，5，6，8，10，11｝，输出｛4，5，6｝，这个用dp可解
2.follow up 例子：输入｛1，4，2，5，3，9，10｝，输出｛1，2，3｝
要求o(nlogn)解法，leetcode上有原题
"""

def longest_consecutive_subarray(list_num):
    longest_subarray =[]
    current_subarray=[]
    for i in range(len(list_num)):
        if len(current_subarray)==0 or list_num[i] - list_num[i-1] == 1:
            current_subarray.append(list_num[i])
            if len(longest_subarray) < len(current_subarray):
                longest_subarray = current_subarray
        else:
            current_subarray = [list_num[i]]

    return longest_subarray

def longest_consecutive_subarray_p2(list_num):
    dict_consec_num = {}
    for num in list_num:
        if num - 1 in dict_consec_num:
            dict_consec_num[num - 1].append(num)
            dict_consec_num[num] = dict_consec_num.pop(num-1)
        else:
            dict_consec_num[num] = [num]
    max_len = 0
    longest_subarray = []
    for _, list_sub_num in dict_consec_num.items():
        if len(list_sub_num) > max_len:
            max_len = len(list_sub_num)
            longest_subarray = list_sub_num
    return longest_subarray


# print longest_consecutive_subarray([1, 4, 5, 6, 8, 10, 11, 12, 13])
print longest_consecutive_subarray_p2([1, 4, 2, 5, 3, 9, 10, 11, 6, 7, 12, 8])
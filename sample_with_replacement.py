# -*- coding: utf-8 -*-
"""
一个k个元素的整数数列，随机sample一个点，然后改成NA，一直sample到全部数字都是NA，让你实现
"""
from random import randint

def sample_with_replacement(input_array):
    len_array = len(input_array)
    for i in range(len_array-1, -1, -1):
        sample_index = randint(0, i)
        input_array[sample_index], input_array[i] =  input_array[i], input_array[sample_index]
    return input_array

print sample_with_replacement([1, 3, 4, 2, 7, 5])


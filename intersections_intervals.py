# -*- coding: utf-8 -*-
"""
大概是2016年10月的电面
给两组 intervals，(假设没组interval里的所有intervals都是没有重叠的，而且是按第一个数字sorted)，  求两组interval中所有的交叉，输出新的一组interval! @$ G" r5 Z2 I6 e7 F- L1 [

例如：
A组：[1, 3], [5,9], [10, 11],
B组：[2,3], [4,6]}

希望得到的输出为：[2,3], [4,6]
"""

class Solution(object):
    def intersect(self, intervals1, intervals2):
        l1, l2 = 0, 0
        intersection_list = []
        for interval1_index in range(l1, len(intervals1)):
            for interval2_index in range(l2, len(intervals2)):
                if intervals2[interval2_index][0]<=intervals1[interval1_index][1] \
                        and intervals1[interval1_index][0] <= intervals2[interval2_index][1]:
                    intersection_list.append([max(intervals1[interval1_index][0], intervals2[interval2_index][0]),
                                              min(intervals1[interval1_index][1], intervals2[interval2_index][1])])

                elif intervals2[interval2_index][0]>intervals1[interval1_index][1]:
                    break
                else:
                    l2 = interval2_index + 1
                    if l2 == len(intervals2):
                        return intersection_list
        return intersection_list

print Solution().intersect([[1, 3], [5,9], [10, 11]], [[2,3], [4,6]])


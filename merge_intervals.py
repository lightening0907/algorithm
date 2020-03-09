"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
"""

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda x: x.start)
        merged_intervals = []
        for interval_index in range(len(intervals)):
            interval = intervals[interval_index]
            if len(merged_intervals) == 0:
                merged_intervals.append(interval)
            else:
                if interval.start <= merged_intervals[-1].end:
                    merged_intervals[-1].end = max(merged_intervals[-1].end, interval.end)
                else:
                    merged_intervals.append(interval)
        return merged_intervals

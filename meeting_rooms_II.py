"""
https://leetcode.com/problems/meeting-rooms-ii/

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
"""
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals, key = lambda x: x[0] ) # ascended, sort by first element
        rooms = [] # store the end time of the meeting
        num_room = 0
        for interval in intervals:
            if len(rooms)==0:
                rooms.append(interval[1])
                num_room += 1
                continue
            for i in range(len(rooms) + 1):
                if i == len(rooms):
                    rooms.append(interval[1])
                    num_room += 1
                    break

                if rooms[i] <= interval[0]:
                    rooms[i] = interval[1]
                    break
        return num_room
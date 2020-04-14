"""
621. Task Scheduler
https://leetcode.com/problems/task-scheduler/

Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.



Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.


Constraints:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""

import copy
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        def _leastInterval(candidates, frozen_tasks, tasks_map):
            len_candidates = len(candidates)
            if not bool(tasks_map):
                return 0
            if len_candidates == 0:
                frozen_tasks.append('None')
                if len(frozen_tasks) > n:
                    de_froz = frozen_tasks.pop(0)
                    if de_froz in tasks_map:
                        candidates.append(de_froz)
                return 1 + _leastInterval(candidates, frozen_tasks, tasks_map)
            else:
                min_interval = None
                for i in range(len_candidates):
                    candidates_copy = copy.deepcopy(candidates)
                    frozen_tasks_copy = copy.deepcopy(frozen_tasks)
                    candidate = candidates_copy.pop(i)
                    frozen_tasks_copy.append(candidate)
                    if len(frozen_tasks_copy) > n:
                        de_froz = frozen_tasks_copy.pop(0)
                        if de_froz in tasks_map:
                            candidates_copy.append(de_froz)
                    tasks_map_copy = copy.deepcopy(tasks_map)
                    if candidate in tasks_map_copy:
                        if tasks_map_copy[candidate] > 1 :
                            tasks_map_copy[candidate] -=1
                        else:
                            del tasks_map_copy[candidate]
                    min_interval_tmp = 1 + _leastInterval(candidates_copy, frozen_tasks_copy, tasks_map_copy)
                    if (min_interval is None) or min_interval_tmp < min_interval:
                        min_interval = min_interval_tmp
                return min_interval

        tasks_map = {}
        for task in tasks:
            if task not in tasks_map:
                tasks_map[task] = 1
            else:
                tasks_map[task] += 1

        candidates = tasks_map.keys()
        frozen_task = []
        return _leastInterval(candidates, frozen_task, tasks_map)


import heapq
class Solution2(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        tasks_map = {}
        for task in tasks:
            if task not in tasks_map:
                tasks_map[task] = -1
            else:
                tasks_map[task] -= 1
        # using a reverse value to create a max heap
        max_h = tasks_map.values()
        heapq.heapify(max_h)
        frozen_list = []
        interval = 0
        while max_h:
            for i in range(n + 1):
                if max_h:
                    largest = heapq.heappop(max_h)
                    largest = - (- largest - 1)
                    if largest < 0:
                        frozen_list.append(largest)
                    interval += 1
                elif len(frozen_list) > 0:
                    interval += 1
                else:
                    break
            while len(frozen_list) > 0:
                heapq.heappush(max_h, frozen_list.pop(0))
        return interval
solution = Solution2()
print(solution.leastInterval(["A","A","A","B","B","B"], 2))
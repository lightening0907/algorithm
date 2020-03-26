"""
207. Course Schedule
https://leetcode.com/problems/course-schedule/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.


Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5
"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        list_courses = [0]*numCourses
        num_prerequisites = len(prerequisites)
        if num_prerequisites == 0:
            return True
        graph = {}
        for p_index, prereq in enumerate(prerequisites):
            if prereq[1] not in graph:
                graph[prereq[1]] = [prereq[0]]
            else:
                graph[prereq[1]].append(prereq[0])

        for i in range(numCourses):
            if i in graph and list_courses[i] ==0:
                dfs = [i]
                path = []
                seen = {}
                while len(dfs) > 0 :
                    node = dfs[-1]
                    # if node in seen and seen[node]:
                    #     return False
                    # path.append(node)
                    #
                    if list_courses[node] == 1:
                        break
                    if (node not in seen or not seen[node]) and node in graph:
                        for next_node in graph[node]:
                            if next_node in seen and seen[next_node]:
                                return False
                            dfs.append(next_node)
                        seen[node] = True
                    else:
                        ab_node = dfs.pop()
                        seen[ab_node] = False
                        list_courses[ab_node] == 1


        return True


from collections import defaultdict

class ClassNode(object):
    def __init__(self):
        self.children = []
        self.num_parents = 0

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # build graph
        num_edge = 0
        graph = defaultdict(ClassNode)
        for pre in prerequisites:
            child, parent = pre[0], pre[1]
            graph[pre[1]].children.append(child)
            graph[pre[0]].num_parents += 1
            num_edge += 1

        # topological sort
        no_dependent_nodes = []
        for node in graph:
            if graph[node].num_parents == 0:
                no_dependent_nodes.append(node)
        while len(no_dependent_nodes) > 0:
            node = no_dependent_nodes.pop()
            if len(graph[node].children) > 0:
                for child in graph[node].children:
                    graph[child].num_parents -=1
                    if graph[child].num_parents ==0:
                        no_dependent_nodes.append(child)
                    num_edge -= 1
        if num_edge > 0:
            return False
        return True
solution = Solution()
print(solution.canFinish(3, [[1,0],[2,1]]))
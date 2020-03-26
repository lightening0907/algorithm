"""
973. K Closest Points to Origin
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)



Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)


Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
"""


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        num_points = len(points)
        if num_points < K:
            return points

        dict_distance_points= {} # distance: list of points
        # dict_distance_count= {} # distance: counts of points with this distance
        distances = []
        for point in points:
            distance_0 = (point[0]**2 + point[1]**2)**0.5
            if distance_0 in dict_distance_points:
                dict_distance_points[distance_0].append([point[0], point[1]])
            else:
                dict_distance_points[distance_0] = [[point[0], point[1]]]
            distances.append(distance_0)

        self.ksmallest(distances, 0, num_points-1, K)
        res = []
        for distance_index in range(K):
            if not( distance_index > 0 and distances[distance_index]==distances[distance_index-1]):
                res.extend(dict_distance_points[distances[distance_index]])
        return res


    def partition(self, distances, l, r):
        i = l
        for j in range(l, r):
            if distances[j] < distances[r]:
                distances[i], distances[j] = distances[j], distances[i]
                i = i + 1
        distances[i], distances[r] = distances[r], distances[i]
        return i

    def ksmallest(self, distances, l, r, K):
        p_index = self.partition(distances, l, r)
        if p_index - l + 1 == K:
            return
        elif p_index -l + 1 < K:
            self.ksmallest(distances, p_index+1, r, K - p_index + l - 1)
        else:
            self.ksmallest(distances, l, p_index-1, K)



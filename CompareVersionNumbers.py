class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        l_v1 = len(version1)
        l_v2 = len(version2)

        ind1_prev,ind1 = 0,0
        ind2_prev,ind2 = 0,0
        while ind1 < l_v1 or ind2 < l_v2:
            while ind1 < l_v1 and version1[ind1] != '.':
                ind1 += 1
            while ind2 < l_v2 and version2[ind2] != '.':
                ind2 += 1

            if ind1>l_v1:
                if 0 < int(version2[ind2_prev:ind2]):
                    return -1
            elif ind2>l_v2:
                if int(version1[ind1_prev:ind1]) > 0:
                    return 1
            elif int(version1[ind1_prev:ind1]) > int(version2[ind2_prev:ind2]):
                return 1
            elif int(version1[ind1_prev:ind1]) < int(version2[ind2_prev:ind2]):
                return -1
            ind1 += 1
            ind1_prev = ind1
            ind2 += 1

            ind2_prev = ind2
        return 0
Solution1 = Solution()
print Solution1.compareVersion("1.0","1")
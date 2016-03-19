# Implement strStr().
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l_hay= len(haystack)
        l_nee = len(needle)
        ind_nee = 0
        if not haystack and not needle: return 0
        if haystack and not needle: return 0
        if l_hay < l_nee: return -1
        for ind_hay in range(l_hay):
            temp_ind_hay = ind_hay
            while temp_ind_hay < l_hay and ind_nee < l_nee:
                if haystack[temp_ind_hay] != needle[ind_nee]:
                    ind_nee = 0
                    break
                else:
                    ind_nee += 1
                    temp_ind_hay +=1
                if ind_nee == l_nee:
                    return ind_hay
                if temp_ind_hay == l_hay:
                    return -1
        # if ind_nee == l_nee: return ind_hay-l_nee+1
        return -1
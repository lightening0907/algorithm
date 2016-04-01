# Write a function to find the longest common prefix string amongst an array of strings.
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        # tem_prefix=''
        for ele_str in strs:
            if not prefix:
                prefix = ele_str
            else:
                for index in range(len(prefix)):
                    if index>len(ele_str)-1 or prefix[index]!=ele_str[index]:
                        index = index-1
                        break
                prefix = prefix[:index+1]
            if not prefix: return prefix
        return prefix




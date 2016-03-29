"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs: return [[]]
        strs.sort()
        dict_anagram = {}
        for str_ele in strs:
            tuple_str_ele = tuple(sorted(str_ele))
            #set_str_ele = tuple(sorted(str_ele))
            if tuple_str_ele in dict_anagram:
                dict_anagram[tuple_str_ele].append(str_ele)
            else:
                dict_anagram[tuple_str_ele]=[str_ele]
        return dict_anagram.values()
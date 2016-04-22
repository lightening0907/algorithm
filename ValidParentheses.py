"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        par_dict ={'(':1,')':-1,'[':2,']':-2,'{':3,'}':-3}
        par_stack = []
        len_s = len(s)
        for index in range(len_s):
            if par_dict[s[index]]>0:
                par_stack.append(s[index])
            else:
                if par_stack and -(par_dict[par_stack[-1]])==(par_dict[s[index]]):
                    del par_stack[-1]
                else: return False
        if not par_stack:
            return True
        else:
            return False
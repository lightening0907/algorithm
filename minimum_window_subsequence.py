"""
727. Minimum Window Subsequence
https://leetcode.com/problems/minimum-window-subsequence/
Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

Example 1:

Input:
S = "abcdebdde", T = "bde"
Output: "bcde"
Explanation:
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of T in the window must occur in order.
"""
class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        len_S = len(S)
        len_T = len(T)
        ans = ""
        substr_stack = []
        min_ans_len = None
        for s_index, s_ele in enumerate(S):
            len_stack = len(substr_stack)
            if len_stack == 0 and s_ele == T[0]:
                if len_T == 1:
                    return T[0]
                substr_stack.append([T[0], 1]) # a list of substring , next index in T to look for
            else:
                over_write_flag = False
                list_index_pop = []
                list_remove = []
                for stack_index in range(len_stack):
                    if s_ele == T[substr_stack[stack_index][1]]:
                        substr_stack[stack_index][0] += s_ele
                        substr_stack[stack_index][1] += 1
                    # elif s_ele == T[substr_stack[stack_index][1] - 1] and s_ele == T[0]:
                    #     substr_stack[stack_index][0] = s_ele
                    #     over_write_flag = True
                    else:
                        substr_stack[stack_index][0] += s_ele
                    if min_ans_len is not None and len(substr_stack[stack_index][0]) >= min_ans_len :
                        list_remove.append(stack_index)
                    # elif substr_stack[stack_index][1] == len_T:
                    #     list_index_pop.append(stack_index)


                while len(list_remove) > 0:
                    substr_stack.pop(list_remove.pop())
                while len(substr_stack) > 0:
                    if substr_stack[0][1] != len_T:
                        break
                    else:
                        potential_ans = substr_stack.pop(0)[0]
                        if min_ans_len is None or min_ans_len > len(potential_ans):
                            ans = potential_ans
                            min_ans_len = len(potential_ans)

                if not over_write_flag and s_ele == T[0]:
                    substr_stack.append([T[0], 1])

        return ans

class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        len_S = len(S)
        len_T = len(T)
        ans = ""
        substr_dict = {} # index indicate next char needed
        min_ans_len = None
        for s_index, s_ele in enumerate(S):
            if not bool(substr_dict) and s_ele == T[0]:
                if len_T == 1:
                    return T[0]
                substr_dict = {1: T[0]}
            else:
                list_keys = substr_dict.keys()
                tmp_substr_dict = {}
                for index_key in list_keys:
                    if min_ans_len is None or len(substr_dict[index_key]) < min_ans_len -1:
                        if s_ele == T[index_key]:
                            string_candidate = substr_dict[index_key]
                            string_candidate =  string_candidate + s_ele
                            if index_key == len_T -1 :
                                ans = string_candidate
                                min_ans_len = len(string_candidate)
                            else:
                                new_key = index_key + 1
                                tmp_substr_dict[new_key] = string_candidate
                            substr_dict.pop(index_key)
                        else:
                            substr_dict[index_key] += s_ele
                    else:
                        substr_dict.pop(index_key)

                for index_key in tmp_substr_dict:
                    if index_key in substr_dict:
                        if len(tmp_substr_dict[index_key]) < len(substr_dict[index_key]):
                            substr_dict[index_key] = tmp_substr_dict[index_key]
                    else:
                        substr_dict[index_key] = tmp_substr_dict[index_key]

                if  s_ele == T[0]:
                    substr_dict[1] = s_ele
        return ans
solution = Solution()
print(solution.minWindow("cnhczmccqouqadqtmjjzl"
,"cm"))

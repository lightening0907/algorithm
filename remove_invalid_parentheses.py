"""
301. Remove Invalid Parentheses
https://leetcode.com/problems/remove-invalid-parentheses/
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # inclusive of the current element
        len_s = len(s)
        if len_s == 0:
            return [""]
        ans = []
        valid_flag, left_right_diff, tot_right, tot_left = self.check_valid_parenthesis(s)
        list_s_dp = [] # a stack of potential solutions [[list of element after exclusion, diff left right]]
        if valid_flag:
            return [s]
        else:
            left_left = 0
            left_right = 0
            for s_index in range(len_s):
                if s_index == 0:
                    list_s_dp.append([[], left_right_diff, tot_right, tot_left, left_left, left_right])
                tmp_list_s_dp = []
                while len(list_s_dp) > 0:
                    list_s_dp_ele = list_s_dp.pop()
                    list_s, left_right_diff, tot_right, tot_left, left_left, left_right = list_s_dp_ele[0], list_s_dp_ele[1], list_s_dp_ele[2], list_s_dp_ele[3], list_s_dp_ele[4], list_s_dp_ele[5]
                    list_s.append(s[s_index])
                    if s[s_index] == '(':
                        left_left +=  1

                    elif  s[s_index] == ')':
                        left_right += 1

                    right_right = tot_right - left_right
                    right_left = tot_left - left_left
                    if left_left >= left_right:

                        if left_left > left_right:

                            if left_right_diff > 0 and s[s_index] == '(':

                                tmp_list_s_dp.append([list_s[:], left_right_diff, tot_right, tot_left, left_left, left_right])

                                list_s.pop()
                                left_left -= 1
                                left_right_diff -= 1
                                tot_left -= 1
                                tmp_list_s_dp.append([list_s[:], left_right_diff, tot_right, tot_left, left_left, left_right])

                            elif  s[s_index] == ')': #(left_right_diff < 0  or (left_right_diff ==0 and right_right > right_left)) and
                                tmp_list_s_dp.append([list_s[:], left_right_diff, tot_right, tot_left, left_left, left_right])
                                list_s.pop()
                                left_right -= 1
                                left_right_diff += 1
                                tot_right -= 1
                                tmp_list_s_dp.append([list_s[:], left_right_diff, tot_right, tot_left, left_left, left_right])
                            else:
                                tmp_list_s_dp.append([list_s[:], left_right_diff, tot_right, tot_left, left_left, left_right])


                        else:
                            if   s[s_index] == ')':#left_right_diff < 0 and
                                tmp_list_s_dp.append([list_s[:], left_right_diff, tot_right, tot_left, left_left, left_right])
                                list_s.pop()
                                left_right -= 1
                                left_right_diff += 1
                                tot_right -= 1
                                tmp_list_s_dp.append([list_s[:], left_right_diff, tot_right, tot_left, left_left, left_right])
                            else:
                                tmp_list_s_dp.append([list_s[:], left_right_diff, tot_right, tot_left, left_left, left_right])
                    else: #left_left < left_right
                        list_s.pop()
                        left_right -= 1
                        left_right_diff += 1
                        tot_right -= 1
                        tmp_list_s_dp.append([list_s[:], left_right_diff, tot_right, tot_left, left_left, left_right])
                list_s_dp = tmp_list_s_dp
            seen_dict = {}
            max_len = 0
            for l_index in range(len(list_s_dp)):
                if list_s_dp[l_index][1] == 0:
                    if len(list_s_dp[l_index][0]) > max_len:
                        max_len = len(list_s_dp[l_index][0])

            for l_index in range(len(list_s_dp)):
                if list_s_dp[l_index][1] == 0:
                    if len(list_s_dp[l_index][0]) == max_len:
                        candidate =''.join(list_s_dp[l_index][0])
                        if candidate not in seen_dict:
                            ans.append(candidate)
                            seen_dict[candidate] = True
            if len(ans) == 0:
                return [""]
            return ans

    def check_valid_parenthesis(self, s):
        len_s = len(s)

        right_left = 0
        right_right = 0
        valid_flag = True
        for s_index in range(len_s-1, -1, -1):
            if s[s_index] == '(':
                right_left += 1
            elif s[s_index] == ')':
                right_right += 1
            if right_left > right_right:
                valid_flag = False
        left_right_diff = right_left  - right_right # difference between left and right, < 0, remove right, > 0 remove right
        if valid_flag and left_right_diff == 0:
            return True, left_right_diff, right_right, right_left
        else:
            return False, left_right_diff, right_right, right_left


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        len_s = len(s)
        if len_s == 0:
            return [""]
        num_invalid_left = 0
        num_invalid_right = 0
        # estimate the total number of invalid left paranthesis and right parathesis to be removed
        for letter in s:
            if letter == "(":
                num_invalid_left += 1
            elif letter == ")":
                if num_invalid_left > 0:
                    num_invalid_left -= 1
                else:
                    num_invalid_right += 1
        self.ans = set()

        def remove_parentheses(left, right, num_invalid_left, num_invalid_right, index, s):
            len_s = len(s)
            if index == len_s:
                if left==right and num_invalid_left ==0 and num_invalid_right ==0:
                    self.ans.add(s)
                    return
            else:
                if s[index] == "(":
                    # remove the ( if we need to remove left
                    if num_invalid_left >0:
                        if index < len_s - 1:
                            remove_parentheses(left, right, num_invalid_left - 1, num_invalid_right, index, s[:index] + s[index+1: ])
                        else:
                            remove_parentheses(left, right, num_invalid_left - 1, num_invalid_right, index, s[:index])
                    # keep the ( as a potential solution
                    remove_parentheses(left + 1, right, num_invalid_left, num_invalid_right, index+1, s)
                elif s[index] == ")":

                    if num_invalid_right > 0:
                        if index < len_s - 1:
                            remove_parentheses(left, right, num_invalid_left, num_invalid_right-1, index, s[:index] + s[index+1: ])
                        else:
                            remove_parentheses(left, right, num_invalid_left, num_invalid_right-1, index, s[:index])
                    # only keep ) if right now there are less ) than ( otherwise we are adding invalid )
                    if left > right:
                        remove_parentheses(left, right + 1, num_invalid_left, num_invalid_right, index+1, s)
                else:
                    remove_parentheses(left, right, num_invalid_left, num_invalid_right, index+1, s)
        remove_parentheses(0, 0, num_invalid_left, num_invalid_right, 0, s)
        return self.ans
solution = Solution()
print(solution.removeInvalidParentheses(")("))







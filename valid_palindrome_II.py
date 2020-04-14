class Solution(object):
    def is_palindrome(self, s):
        len_s = len(s)
        if len_s == 0:
            return False
        left = 0
        right = len_s - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -=1
            else:
                return False
        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        len_s = len(s)
        if len_s == 0:
            return False
        left = 0
        right = len_s - 1
        modified = False
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -=1
            elif modified and s[left] != s[right]:
                return False
            elif not modified and s[left] != s[right]:
                return self.is_palindrome(s[left + 1: right+1]) or self.is_palindrome(s[left: right])
        return True

solution = Solution()
print(solution.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))
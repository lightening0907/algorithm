__author__ = 'ChiYuan'
class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        if s =='' and p=='':
            return True
        elif p =='' and s!='':
            return False
        elif len(p)==1:
            if len(s)==1 and (s==p or p=='.'):
                return True
            else:
                return False
        elif p[1] == '*':
            if s=='':
                return self.isMatch(s,p[2:])
            if p[0] == s[0] or p[0] == '.':
                if len(s)>1:
                    return (self.isMatch(s[1:],p) or self.isMatch(s,p[2:]))
                else:
                    return (self.isMatch("",p) or self.isMatch(s,p[2:]))

            elif p[0] != s[0]:
                return self.isMatch(s,p[2:])
        elif s=='': return False
        elif p[0]==s[0] or p[0] == '.':
            if len(s)>1:
                return self.isMatch(s[1:],p[1:])
            else:
                return self.isMatch("",p[1:])
        else:
            return False

print(Solution().isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))
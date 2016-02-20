__author__ = 'ChiYuan'
class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def revstring(self,w):
        ls = len(w)
        i = 0
        while i<(ls-1-i):
            w[i],w[ls-1-i]=w[ls-1-i],w[i]
            i += 1
        return w

    def reverseWords(self,s):
        if s=="":
            return
        self.revstring(s)

        lws = len(s) #length of the whole string
        itemp = -1
        i = 0
        while i < lws:
            if s[i]==" ":
                s[itemp+1:i] = self.revstring(s[itemp+1:i])
                itemp = i
            if i == lws-1:
                s[itemp+1:] = self.revstring(s[itemp+1:])
                print ("bzz")
            i += 1
if __name__ == '__main__':
    s= ["h","i","!"]
    Solution().reverseWords(s)
    print(s)
__author__ = 'ChiYuan'
def revstring(self,w):
        ls = len(w)
        i = 0
        while i<(ls-1-i):
            w[i],w[ls-1-i]=w[ls-1-i],w[i]
            i += 1
        return w

def reverseWords(self,s):
        s = revstring(self,s)
        lws = len(s) #length of the whole string
        itemp = 0
        i = 0
        while i < lws:
            if s[i]==" ":
                if itemp == i-1:
                    s = s[:i]+s[i+1:]
                    lws -= 1
                else:
                    s[itemp+1:i] = revstring(self,s[itemp+1:i])
                itemp = i
            i += 1
        return s


print(reverseWords("s",["s","h","g"]))


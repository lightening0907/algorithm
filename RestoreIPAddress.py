class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.len_s = len(s)
        self.s = s
        return self.restore(0,4)

    def restore(self,index,chunk):
        len_substr = self.len_s - index
        if len_substr < chunk or len_substr > chunk*3: return []
        if chunk == 1:
            if self.s[index:]=='0' or ( self.s[index]!='0'and int(self.s[index:])<=255):
                return [self.s[index:]]
            else:
                return []
        valid_ip = []

        for i in range(1,4):
            rest = []
            if i+index > self.len_s-1:
                return valid_ip
            if int(self.s[index:i+index])<=255:
                rest = self.restore(i+index,chunk-1)
            for item in rest:
                valid_ip.append(self.s[index:i+index]+'.'+item)
            if i==1 and self.s[index]=='0':
                return valid_ip
        return valid_ip

Solution1 = Solution()
print Solution1.restoreIpAddresses("0000")
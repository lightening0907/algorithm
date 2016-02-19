
#Integer to Roman
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_v=[1000,500,100,50,10,5,1]
        roman_l=["M","D","C","L","X","V","I"]
        output=""
        i = 0
        while i<7:
            div = num/roman_v[i]

            if div == 0 and i%2 == 0 and i < 5 and roman_v[i] - num <= roman_v[i+2]:
                output = output + (roman_l[i+2]+roman_l[i])
                num = num - (roman_v[i]-roman_v[i+2])
                i += 1
            elif div>0:
                if div==4 and i%2==0:
                    output = output + (roman_l[i]+roman_l[i-1])

                else:
                    output = output + roman_l[i]*div
                num = num%roman_v[i]
                if not(num/roman_v[i] == 0 and i%2 == 0 and i < 5 and roman_v[i] - num <= roman_v[i+2]): i +=1
            else: i +=1
        return output


class Solution2(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_v=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        roman_l=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        l_r = len(roman_l)
        output = ""
        while num>0:
            for i in range(l_r):
                div = num/roman_v[i]
                if div>0:
                    output = output + roman_l[i]*div
                    num = num - div*roman_v[i]

        return output

Solution1=Solution()
print Solution1.intToRoman(19)

#roman to integer
class Solution3(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman ={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        l_s = len(s)
        ret = 0
        for i in range(l_s):
            if i< l_s - 1 and roman[s[i]]<roman[s[i+1]]:
                ret = ret - roman[s[i]]
            else: ret = ret+roman[s[i]]
        return ret
__author__ = 'ChiYuan'
def stringsum(str1,str2):
    lstr1 = len(str1)
    lstr2 = len(str2)
    sum_str = ""
    max_l = max(lstr1,lstr2)
    if lstr1<lstr2:
        str1 = str1.rjust(lstr2,'0')
    elif lstr1>lstr2:
        str2 = str2.rjust(lstr1,'0')

    i = max_l-1
    c_over = 0
    while i >= 0 or c_over>0:
        if i >=0:
            temp_v = int(str1[i])+int(str2[i])+c_over
        else:
            temp_v = c_over
        if temp_v >= 10:
            c_over = 1
            sum_str = str(temp_v-10) + sum_str
        else:
            c_over = 0
            sum_str = str(temp_v) + sum_str




        i -=1
    return sum_str

print(stringsum('999','11'))



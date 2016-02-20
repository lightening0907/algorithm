__author__ = 'ChiYuan'
def atoi(str1):
    str_num={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    num1 = 0
    for i in range(len(str1)):
        if str1[i] in str_num:
            num1 = num1*10+str_num[str1[i]]
    return num1

print(atoi('1234897203462734538208479'))
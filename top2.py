__author__ = 'ChiYuan'
name = open("C:\\Users\\ChiYuan\\Documents\\python\\name.txt",'r')
sl = []#tuple of the first two largest number
t_l = []#temporal line
for line in name.readlines():
    line = line.strip('\n')
    t_l = line.split(',')

    if t_l[1] == 'F':
        t_l[2] = int(t_l[2])
        if len(sl) == 0:
            sl.append([t_l[0],t_l[2]])
        elif len(sl) == 1:
            #sl.insert(t_l[2]>=sl[0][1],[t_l[0],t_l[2]])
            sl.append([t_l[0],t_l[2]])
        elif t_l[2]-sl[1][1]>0:
            sl[0][0] = sl[1][0]
            sl[0][1] = sl[1][1]
            sl[1][1]=t_l[2]
            sl[1][0]=t_l[0]

        elif t_l[2]-sl[0][1]>0:
            sl[0][1]=t_l[2]
            sl[0][0]=t_l[0]

print (sl)
name.close()
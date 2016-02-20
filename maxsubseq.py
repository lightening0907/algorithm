__author__ = 'ChiYuan'
#calculating the maximum sum of a subsequence
def maxsub(m):
    lm = len(m) #length of m
    t_sum = 0 #sum of a subsequence
    t_max = 0 #a temporary maximum sum
    t_mn = m[0]#the maximum element
    for i in range(lm):
        t_v = t_sum+m[i] #sum of the subsequence that including the new value m[i]
        if m[i]>t_mn: t_mn=m[i]
        if m[i]>=0:
            t_sum = t_v
            if t_max < t_sum:
                t_max = t_sum
        else:
            if t_v>=0:
               t_sum = t_v
            else:
               t_sum = 0
    return max(t_max,t_sum,t_mn)


print(maxsub([1, 2, -4, 1, 3, -2, 3, -1]))




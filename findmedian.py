__author__ = 'ChiYuan'
#
# Given a list of numbers, L, find a number, x, that
# minimizes the sum of the absolute value of the difference
# between each element in L and x: SUM_{i=0}^{n-1} |L[i] - x|
#
# Your code should run in Theta(n) time
#
from random import randint
def minimize_absolute(L):
    global cl
    global cr
    global ll
    global fl
    ll = len(L)
    if ll ==1:
        return L[0]
    i = randint(0,ll-1)
    fl = (ll-1)//2
    cl = 0#left of the partition
    cr = 0#right of the partition
    return partition(L,L[i])
   # print ('x is %d'%x)
    # your code here


def partition(L,x):
    global cl
    global cr
    global ll
    global fl
    lefs = []
    rigs = []
    for i in L:
        if i<x:
            lefs.append(i)
        elif i>x:
            rigs.append(i)
    lfl = len(lefs)
    cl = cl + lfl
    rgl = len(rigs)
    cr = cr + rgl
    print (lefs,rigs,cl,cr,fl)
    if cl==fl or cr==fl:
        print ("find it")
        print (x)
        return x
    elif cl > fl:
        if len(lefs) == 1:
            return lefs[0]
        else:
            #print (lfl)
            xt = randint(0,lfl-1)
            cl = cl - lfl
            cr += 1
            return partition(lefs,lefs[xt])
    elif cl < fl:
        if len(rigs) == 1: return rigs[0]
        else:
            #print (rgl)
            xt = randint(0,rgl-1)
            cr = cr - rgl
            cl +=1
            return partition(rigs,rigs[xt])

L=[1,5,3,4,6,11]
print (len(L))
print (minimize_absolute(L))
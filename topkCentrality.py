__author__ = 'ChiYuan'
from random import randrange
import csv
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def centrality(G, v):
    distance_from_start = {}
    open_list = [v]
    distance_from_start[v] = 0
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[current] + 1
                open_list.append(neighbor)
    return float(sum(distance_from_start.values()))/len(distance_from_start)

def partition(L,v):
    smaller = []
    bigger = []
    for i in L:
        if i[1] < v: smaller.append(i)
        elif i[1] > v: bigger.append(i)
    return(bigger,smaller)

def topk(L,k):
    v = randrange(len(L))
    (left,right)=partition(L,L[v][1])
    if len(left) == k-1: return (L[v][0],L[v][1])
    elif len(left) > k-1:
        print (left)
        return topk(left,k)
    elif len(left) < k-1: return topk(right,k-2-len(left))

t_l2 = []
t_l = []
G = {}
act = {}


with open('C:\\Users\\ChiYuan\\Documents\\python\\movie.tsv','r') as movie:
    movie = csv.reader(movie,delimiter='\t')

    for t_l in movie:
        t_l2.append([t_l[0],t_l[1]+t_l[2]])
        make_link(G,t_l[0],t_l[1]+t_l[2])
        if t_l[0] not in act: act[t_l[0]] = 0

for pp in act:
    act[pp] = centrality(G,pp)

actl = list(zip(act.keys(),act.values()))

print (topk(actl,20))


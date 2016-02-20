__author__ = 'ChiYuan'
#
# The code below uses a linear
# scan to find the unfinished node
# with the smallest distance from
# the source.
#
# Modify it to use a heap instead
#
'''
def shortest_dist_node(dist):
    best_node = 'undefined'
    best_value = 1000000
    for v in dist:
        if dist[v] < best_value:
            (best_node, best_value) = (v, dist[v])
    return best_node
'''
def remove_min(L,nd,nl):
    # your code here
    hl = len(L)
    L[0] = L[hl-1]
    del L[hl-1]
    nl[nd[hl-1]] = 0
    del nl[nd[0]]
    nd[0] = nd[hl-1]
    del nd[hl-1]

    down_heapify(L,nd,nl,0)
    return L

def parent(i):
    return (i-1)//2
def left_child(i):
    return 2*i+1
def right_child(i):
    return 2*i+2
def is_leaf(L,i):
    return (left_child(i) >= len(L)) and (right_child(i) >= len(L))
def one_child(L,i):
    return (left_child(i) < len(L)) and (right_child(i) >= len(L))

def down_heapify(L,nd,nl,i):
    # If i is a leaf, heap property holds
    if is_leaf(L, i):
        return
    # If i has one child...
    if one_child(L, i):
        # check heap property
        if L[i] > L[left_child(i)]:
            # If it fails, swap, fixing i and its child (a leaf)
            (L[i], L[left_child(i)]) = (L[left_child(i)], L[i])
            (nd[i],nd[left_child(i)]) = (nd[left_child(i)],nd[i])
            (nl[nd[i]],nl[nd[left_child(i)]]) = (nl[nd[left_child(i)]],nl[nd[i]])
        return
    # If i has two children...
    # check heap property
    if min(L[left_child(i)], L[right_child(i)]) >= L[i]:
        return
    # If it fails, see which child is the smaller
    # and swap i's value into that child
    # Afterwards, recurse into that child, which might violate
    if L[left_child(i)] < L[right_child(i)]:
        # Swap into left child
        (L[i], L[left_child(i)]) = (L[left_child(i)], L[i])
        (nd[i],nd[left_child(i)]) = (nd[left_child(i)],nd[i])
        (nl[nd[i]],nl[nd[left_child(i)]]) = (nl[nd[left_child(i)]],nl[nd[i]])
        down_heapify(L,nd,nl,left_child(i))
        return
    else:
        (L[i], L[right_child(i)]) = (L[right_child(i)], L[i])
        (nd[i],nd[right_child(i)]) = (nd[right_child(i)],nd[i])
        (nl[nd[i]],nl[nd[right_child(i)]]) = (nl[nd[right_child(i)]],nl[nd[i]])
        down_heapify(L,nd,nl,right_child(i))
        return

def up_heapify(L,nd,nl,i):
    # your code here
    if i==0:
        return
    if L[parent(i)]<L[i]:
        return
    elif L[parent(i)]>L[i]:
        (L[parent(i)],L[i])=(L[i],L[parent(i)])
        (nd[parent(i)],nd[i]) = (nd[i],nd[parent(i)])
        (nl[nd[parent(i)]],nl[nd[i]]) = (nl[nd[i]],nl[nd[parent(i)]])
        up_heapify(L,nd,nl,parent(i))
        return

def dijkstra(G,v):
    dist_so_far = []#list of distances
    n_dist = [] #lists of the nodes corresponding to the distances
    n_loc = {} #dictionary of the nodes, and its location in the heap
    dist_so_far.append(0)
    n_dist.append(v)
    n_loc[v] = 0
    final_dist = {}
    while len(final_dist) < len(G):
        #w = shortest_dist_node(dist_so_far)
        w = n_dist[0]
        # lock it down!
        final_dist[w] = dist_so_far[0]
        remove_min(dist_so_far,n_dist,n_loc)

        for x in G[w]:
            if x not in final_dist:
                if x not in n_dist:
                    #dist_so_far[x] = final_dist[w] + G[w][x]
                    dist_so_far.append(final_dist[w] + G[w][x])
                    n_dist.append(x)
                    n_loc[x] = len(n_dist) - 1
                    up_heapify(dist_so_far,n_dist,n_loc,n_loc[x])
                elif final_dist[w] + G[w][x] < dist_so_far[n_loc[x]]:
                    dist_so_far[n_loc[x]] = final_dist[w] + G[w][x]
                    up_heapify(dist_so_far,n_dist,n_loc,n_loc[x])
    return final_dist

############
#
# Test

def make_link(G, node1, node2, w):
    if node1 not in G:
        G[node1] = {}
    if node2 not in G[node1]:
        (G[node1])[node2] = 0
    (G[node1])[node2] += w
    if node2 not in G:
        G[node2] = {}
    if node1 not in G[node2]:
        (G[node2])[node1] = 0
    (G[node2])[node1] += w
    return G


def test():
    # shortcuts
    (a,b,c,d,e,f,g) = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
    triples = ((a,c,3),(c,b,10),(a,b,15),(d,b,9),(a,d,4),(d,f,7),(d,e,3),
               (e,g,1),(e,f,5),(f,g,2),(b,f,1))
    G = {}
    for (i,j,k) in triples:
        make_link(G, i, j, k)

    dist = dijkstra(G, a)
    print (dist[g])
    assert dist[g] == 8 #(a -> d -> e -> g)
    assert dist[b] == 11 #(a -> d -> e -> g -> f -> b)

test()
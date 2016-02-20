__author__ = 'ChiYuan'
import csv
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def read_graph(filename):
    # Read an undirected graph in CSV format. Each line is an edge
    tsv = csv.reader(open(filename), delimiter='\t')
    G = {}
    cp = []
    for (node1, node2) in tsv:
        make_link(G, node1, node2)
        if node1 not in cp:
            cp.append(node1)
    return G,cp

(marvelG,cp) = read_graph("C:\\Users\\ChiYuan\\Documents\\python\\marvel.tsv")

nG = {}
lcp = len(cp)
for i in range(lcp-1):
    for j in range(i+1,lcp):
        for mv in marvelG[cp[i]].keys():
            if mv in marvelG[cp[j]].keys():
                if cp[i]+" "+cp[j] not in nG:
                    nG[cp[i]+" "+cp[j]] = 1
                else:
                    nG[cp[i]+" "+cp[j]] += 1

nGk = list(nG.keys())
nGv = list(nG.values())
mGk = nGk[0]
mGv = nG[mGk]
for i in nGk:
    if nG[i] > mGv:
        mGV = nG[i]
        mGk = i
#print (nG)
print (mGV,mGk)
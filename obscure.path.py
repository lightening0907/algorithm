__author__ = 'ChiYuan'
#
# Another way of thinking of a path in the Kevin Bacon game
# is not about finding *short* paths, but by finding paths
# that don’t use obscure movies.  We will give you a
# list of movies along with their obscureness score.
#
# For this assignment, we'll approximate obscurity
# based on the multiplicative inverse of the amount of
# money the movie made.  Though, its not really important where
# the obscurity score came from.
#
# Use the the imdb-1.tsv and imdb-weights.tsv files to find
# the obscurity of the “least obscure”
# path from a given actor to another.
# The obscurity of a path is the maximum obscurity of
# any of the movies used along the path.
#
# You will have to do the processing in your local environment
# and then copy in your answer.
#
# Hint: A variation of Dijkstra can be used to solve this problem.
#

# Change the `None` values in this dictionary to be the obscurity score
# of the least obscure path between the two actors

    # Read an undirected graph in CSV format. Each line is an edge
import csv

def make_link(G, node1, node2,node3):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = node3
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = node3
    return G


imdb = csv.reader(open('C:\\Users\\ChiYuan\\Documents\\python\\imdb-1.tsv'), delimiter='\t')
imdb_weight = csv.reader(open('C:\\Users\\ChiYuan\\Documents\\python\\imdb-weights.tsv'), delimiter='\t')
obs = {}
for (n1,n2,n3) in imdb_weight:
    obs[n1+" "+n2]= float(n3)

G = {}

for (node1, node2,node3) in imdb:
    make_link(G, node1, node2+ " "+node3,obs[node2+ " "+node3])

#print (G['Kamiki, Ryûnosuke'])

def shortest_dist_node(dist):
    best_node = 'undefined'
    best_value = 1000000
    for v in dist:
        if dist[v] < best_value:
            (best_node, best_value) = (v, dist[v])
    return best_node

def dijkstra(G,v1,v2):
    dist_so_far = {}
    dist_so_far[v1] = 0
    final_dist = {}
    while v2 not in final_dist:
        w = shortest_dist_node(dist_so_far)
        # lock it down!
        final_dist[w] = dist_so_far[w]
        del dist_so_far[w]
        for x in G[w]:
            if x not in final_dist:
                if x not in dist_so_far:
                    dist_so_far[x] = max(final_dist[w],G[w][x])
                elif max(final_dist[w], G[w][x]) < dist_so_far[x]:
                    dist_so_far[x] = max(final_dist[w], G[w][x])
    return final_dist[v2]

answer = {(u'Boone Junior, Mark', u'Del Toro, Benicio'): None,
          (u'Braine, Richard', u'Coogan, Will'): None,
          (u'Byrne, Michael (I)', u'Quinn, Al (I)'): None,
          (u'Cartwright, Veronica', u'Edelstein, Lisa'): None,
          (u'Curry, Jon (II)', u'Wise, Ray (I)'): None,
          (u'Di Benedetto, John', u'Hallgrey, Johnathan'): None,
          (u'Hochendoner, Jeff', u'Cross, Kendall'): None,
          (u'Izquierdo, Ty', u'Kimball, Donna'): None,
          (u'Jace, Michael', u'Snell, Don'): None,
          (u'James, Charity', u'Tuerpe, Paul'): None,
          (u'Kay, Dominic Scott', u'Cathey, Reg E.'): None,
          (u'McCabe, Richard', u'Washington, Denzel'): None,
          (u'Reid, Kevin (I)', u'Affleck, Rab'): None,
          (u'Reid, R.D.', u'Boston, David (IV)'): None,
          (u'Restivo, Steve', u'Preston, Carrie (I)'): None,
          (u'Rodriguez, Ramon (II)', u'Mulrooney, Kelsey'): None,
          (u'Rooker, Michael (I)', u'Grady, Kevin (I)'): None,
          (u'Ruscoe, Alan', u'Thornton, Cooper'): None,
          (u'Sloan, Tina', u'Dever, James D.'): None,
          (u'Wasserman, Jerry', u'Sizemore, Tom'): None}




# Here are some test cases.
# For example, the obscurity score of the least obscure path
# between 'Ali, Tony' and 'Allen, Woody' is 0.5657
test = {(u'Ali, Tony', u'Allen, Woody'): 0.5657,
        (u'Auberjonois, Rene', u'MacInnes, Angus'): 0.0814,
        (u'Avery, Shondrella', u'Dorsey, Kimberly (I)'): 0.7837,
        (u'Bollo, Lou', u'Jeremy, Ron'): 0.4763,
        (u'Byrne, P.J.', u'Clarke, Larry'): 0.109,
        (u'Couturier, Sandra-Jessica', u'Jean-Louis, Jimmy'): 0.3649,
        (u'Crawford, Eve (I)', u'Cutler, Tom'): 0.2052,
        (u'Flemyng, Jason', u'Newman, Laraine'): 0.139,
        (u'French, Dawn', u'Smallwood, Tucker'): 0.2979,
        (u'Gunton, Bob', u'Nagra, Joti'): 0.2136,
        (u'Hoffman, Jake (I)', u'Shook, Carol'): 0.6073,
        (u'Kamiki, Ryûnosuke', u'Thor, Cameron'): 0.3644,
        (u'Roache, Linus', u'Dreyfuss, Richard'): 0.6731,
        (u'Sanchez, Phillip (I)', u'Wiest, Dianne'): 0.5083,
        (u'Sheppard, William Morgan', u'Crook, Mackenzie'): 0.0849,
        (u'Stan, Sebastian', u'Malahide, Patrick'): 0.2857,
        (u'Tessiero, Michael A.', u'Molen, Gerald R.'): 0.2056,
        (u'Thomas, Ken (I)', u'Bell, Jamie (I)'): 0.3941,
        (u'Thompson, Sophie (I)', u'Foley, Dave (I)'): 0.1095,
        (u'Tzur, Mira', u'Heston, Charlton'): 0.3642}

for i in test:
    print (i,dijkstra(G,i[0],i[1]))

for i in answer:
    answer[i]= dijkstra(G,i[0],i[1])
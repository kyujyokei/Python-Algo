from heapdict import heapdict
from collections import defaultdict

def shortest(n, edges):

    ad_list = defaultdict(lambda : [])
    hd = heapdict()
    visited = dict()

    for v, u, c in edges:
        ad_list[v].append([u, c])
        ad_list[u].append([v, c])


    hd[0] = [0,[0]]
    while hd:
        obj = hd.popitem()
        curr, [dist, path] = obj
        visited[curr] = [dist, path]
        if curr == n-1: break
        for u, c in ad_list[curr]:
            if u not in visited and (u not in hd or hd[u][0] > c + dist):
                hd[u] = [c + dist, path + [u]]
    return visited[n-1]



def generate_seq(k,length,seed):
    import random; random.seed(seed);
    return [tuple(sorted(random.sample(range(k),2))+[random.randint(5,10)]) for _ in range(length)]
# dense_tuples = generate_seq(1000, 50000, 1)
tuples_1 = generate_seq(5000, 5000, 1)
# tuples_2 = generate_seq(5000, 50000, 4)

# print(tuples_1)
# [(0, 1, 7), (0, 3, 8), (3, 4, 6), (0, 3, 5), (3, 4, 9)]
print(shortest(5000,tuples_1))
# 1. [WILL BE GRADED]
#    Dijkstra (see CLRS 24.3 and DPV 4.4)
#
#    Given an undirected graph, find the shortest path from source (node 0)
#    to target (node n-1).
#
#    Edge weights are guaranteed to be non-negative, since Dijkstra doesn't work
#    with negative weights, e.g.
#
#        3
#    0 ------ 1
#      \    /
#     2 \  / -2
#        \/
#        2
#
#    in this example, Dijkstra would return length 2 (path 0-2),
#    but path 0-1-2 is better (length 1).
#
#    For example (return a pair of shortest-distance and shortest-path):
#
#        1
#    0 ------ 1
#      \    /  \
#     5 \  /1   \6
#        \/   2  \
#        2 ------ 3
#
print(shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
#    (4, [0,1,2,3])
# print(shortest(6,[(0,1,3),(0,2,1),(0,3,2),(2,3,1),(1,3,1),(1,4,1),(3,4,4),(4,5,3),(2,4,8)]))
#
#    [UPDATE] Tiebreaking: arbitrary. Any shortest path would do.
#
#    Filename: dijkstra.py
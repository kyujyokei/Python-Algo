import random
import heapq
import timeit

def nbesta(a, b):
    l = len(a)
    list = []
    for i in a:
        for j in b:
            list.append([i,j])
    list.sort(key = lambda tup: tup[0]+tup[1])
    return list[:l]


def nbestb(a, b):
    l = len(a)
    list = []
    for i in a:
        for j in b:
            list.append([[i, j], i+j])
    q = qselect(len(a), list)
    # print(list)
    # print(q)
    res = [ x[0] for x in list if x[1] <= q ]
    return res[:l]

def nbestc(a,b):
    l = len(a)
    visited = []
    pq = []
    a.sort()
    b.sort()
    pq.append([a[0]+b[0],[0,0]])

    while len(visited) < len (a):
        curr = heapq.heappop(pq)
        visited.append(curr)
        right_p = [curr[1][0]+1,curr[1][1]]
        right = [a[right_p[0]]+b[right_p[1]], right_p]
        down_p = [curr[1][0], curr[1][1]+1]
        down = [a[down_p[0]]+b[down_p[1]], down_p]

        if right not in pq: heapq.heappush(pq,right)
        if down not in pq: heapq.heappush(pq,down)
    res = []
    for d, [i,j] in visited:
        res.append([a[i],b[j]])
    # print(res)
    return res

# def _append(i,j,d):


      # if [[i,j],d] not in reachable:







def qselect(idx, a):
    if a == [] or idx > len(a) or idx < 1:
        return []
    else:
        r = random.randint(0,len(a)-1)
        a[0], a[r] = a[r], a[0]
        # print(a[0],a[r])
        pivot = a[0][1]
        # print("PIVOT: ",pivot)
        left = [x for x in a if x[1] < pivot]
        l_len = len(left)

        if idx == l_len + 1:
            return pivot
        elif idx < l_len + 1:
            return qselect(idx, left)
        else:
            right = [x for x in a[1:] if x[1] >= pivot]
            return qselect(idx-l_len-1, right)





#    Given two lists A and B, each with n integers, return
#    a sorted list C that contains the smallest n elements from AxB:
#
#      AxB = { (x, y) | x in A, y in B }
#
#    i.e., AxB is the Cartesian Product of A and B.
#
#    ordering:  (x,y) < (x',y') iff. x+y < x'+y' or (x+y==x'+y' and y<y')
#
#    You need to implement three algorithms and compare:
#
#    (a) enumerate all n^2 pairs, sort, and take top n.
#    (b) enumerate all n^2 pairs, but use qselect from hw1.
#    (c) Dijkstra-style best-first, only enumerate O(n) (at most 2n) pairs.
#        Hint: you can use Python's heapq module for priority queue.
#
#    Q: What are the time complexities of these algorithms?
#
a, b = [4, 1, 5, 3], [2, 6, 3, 4]

# nbestb(a, b)   # algorithm (b), slow

# nbestc(a, b)   # algorithm (c), fast

#    [(1, 2), (1, 3), (3, 2), (1, 4)]
#
#    Filename: nbest.py
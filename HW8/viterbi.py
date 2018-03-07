from collections import defaultdict

def longest(n, lis):
    ad_list = defaultdict(list)
    indg = dict()
    queue = []
    res = []
    def map(lis):
        for x in lis:
            start, end = x
            if start not in indg: indg[start] = 0
            if end not in indg:
                indg[end] = 1
            else:
                indg[end] = indg[end] + 1
            ad_list.setdefault(start, []).append(end)

    map(lis)

    for i in indg:
        if indg[i] == 0: queue.append(i)

    while queue:
        node = queue.pop(0)
        res += [node]
        if node in ad_list:
            for i in ad_list[node]:
                indg[i] -= 1
                if indg[i] == 0: queue.append(i)

    order = res
    paths = {}
    max = (0,[])
    if order == None: return None
    for i in order:
        # print(type(ad_list))
        if i in ad_list:
            if i not in paths:
                paths[i] = (0, [i])

            for x in ad_list[i]:
                if x not in paths:
                    paths[x] = (0, [x])
                last_sum, last_path = paths[i]
                if last_sum + 1 > paths[x][0]:
                    paths[x] = (last_sum + 1, last_path + [x])
                    if paths[x] > max: max = paths[x]
    return max[0],max[1]



# 3. [WILL BE GRADED]
#    Viterbi Algorithm For Longest Path in DAG (see DPV 4.7, [2], CLRS problem 15-1)
#
#    Recall that the Viterbi algorithm has just two steps:
#    a) get a topological order (use problem 1 above)
#    b) follow that order, and do either forward or backward updates
#
#    This algorithm captures all DP problems on DAGs, for example,
#    longest path, shortest path, number of paths, etc.
#
#    In this problem, given a DAG (guaranteed acyclic!), output a pair (l, p)
#    where l is the length of the longest path (number of edges), and p is the path. (you can think of each edge being unit cost)
#
#    e.g., for the above example:
#
# print(longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
#    (5, [0, 2, 3, 4, 5, 6])


#
# def generate_seq(k,length):
#     import random; random.seed(1);
#     return [tuple(sorted(random.sample(range(k),2))) for _ in range(length)]
#
# tuples = generate_seq(20000, 31000)
# print(len(tuples), tuples)
#
# print(longest(len(tuples),tuples))

#
#    Tie-breaking: arbitrary. any longest path is fine.
#
#    Filename: viterbi.py
#
#    Note: you can use this program to solve LIS, TSP, knapsacks, MIS, etc.
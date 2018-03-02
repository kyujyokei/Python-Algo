def longest(n, list):
    order, ad_list = topol(n, list)
    paths = {}

    if order == None: return None
    # print(ad_list)
    for i in order:
        if i in ad_list:
            paths.setdefault(i, []).append([0, [i]])
            for x in ad_list[i]:
                # print(paths[i][0][1])
                print(i, paths[i])
                last_sum, last_path = paths[i][0]
                paths[x] = [last_sum + 1, last_path + [x]]



        print(paths, i)
    return 0




def topol (n, list):
    ad_list = dict()
    indg = dict()
    queue = []
    res = []

    def map (list):
        for x in list:
            start, end = x
            if start not in indg: indg[start] = 0
            if end not in indg: indg[end] = 1
            else: indg[end] = indg[end] + 1
            ad_list.setdefault(start, []).append(end)

    map(list)

    for i in indg:
        if indg[i] == 0: queue.append(i)

    while queue:

        node = queue.pop(0)
        res += [node]
        if node in ad_list:
            for i in ad_list[node]:
                indg[i] -= 1
                if indg[i] == 0: queue.append(i)
    return res, ad_list if len(res) == n else None


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
longest(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)])
#    (5, [0, 2, 3, 4, 5, 6])
#
#    Tie-breaking: arbitrary. any longest path is fine.
#
#    Filename: viterbi.py
#
#    Note: you can use this program to solve LIS, TSP, knapsacks, MIS, etc.
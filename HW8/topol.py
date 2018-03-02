

def order (n, list):
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
        if indg[i] == 0:
            queue.append(i)

    while queue:

        node = queue.pop(0)
        res += [node]
        if node in ad_list:
            for i in ad_list[node]:
                indg[i] -= 1
                if indg[i] == 0: queue.append(i)

    return res if len(res) == n else None


# Topological Sort
#
#    For a given directed graph, output a topological order if it exists.
#
#    Tie-breaking: ARBITRARY tie-breaking. This will make the code
#    and time complexity analysis a lot easier.
#
#    e.g., for the following example:
#
#      0 --> 2 --> 3 --> 5 --> 6
#         /    \   |  /    \
#        /      \  v /      \
#      1         > 4         > 7
#
print(order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
#    [0, 1, 2, 3, 4, 5, 6, 7]
#
#    If we flip the (3,4) edge:
#
print(order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
#    [0, 1, 2, 4, 3, 5, 6, 7]
#
#    If there is a cycle, output None
#
print(order(4, [(0,1), (1,2), (2,1), (2,3)]))

print(order(7, [(0,1), (1,2), (1,3), (2,4), (3,4), (3,5), (2,6), (4,6), (6,5), (4,5)]))
#    None
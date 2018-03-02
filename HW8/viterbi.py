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
#    >>> longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])
#    (5, [0, 2, 3, 4, 5, 6])
#
#    Tie-breaking: arbitrary. any longest path is fine.
#
#    Filename: viterbi.py
#
#    Note: you can use this program to solve LIS, TSP, knapsacks, MIS, etc.
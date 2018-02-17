def best(w, objs):
    return 0





# 1. Unbounded Knapsack
#
#    You have n items, each with weight w_i and value v_i, and has infinite copies.
#    **All numbers are positive integers.**
#    What's the best value for a bag of W?
#
#    >>> best(3, [(2, 4), (3, 5)])
#    (5, [0, 1])
#
#    the input to the best() function is W and a list of pairs (w_i, v_i).
#    this output means to take 0 copies of item 1 and 1 copy of item 2.
#
#    tie-breaking: *reverse* lexicographical: i.e., [1, 0] is better than [0, 1]:
#    (i.e., take as much from item 1 as possible, etc.)
#
#    >>> best(3, [(1, 5), (1, 5)])
#    (15, [3, 0])
#
#    >>> best(3, [(1, 2), (1, 5)])
#    (15, [0, 3])
#
#    >>> best(3, [(1, 2), (2, 5)])
#    (7, [1, 1])
#
#    >>> best(58, [(5, 9), (9, 18), (6, 12)])
#    (114, [2, 4, 2])
#
#    >>> best(92, [(8, 9), (9, 10), (10, 12), (5, 6)])
#    (109, [1, 1, 7, 1])
#
#    Q: What are the time and space complexities?
#
#    filename: knapsack_unbounded.py
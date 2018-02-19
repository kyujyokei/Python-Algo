def best(x, items):
    n = len(items)
    items.insert(0, (0, 0))
    def_list = [0 for a in range(0,len(items)-1)]
    opt = [[[0,def_list] for i in range(0,x+1)] for j in range(0,n+1)]



    for i in range(1, n+1):
        weight, value = items[i][0],items[i][1]
        for j in range(1,x+1):
            temp = []
            list = [0 for a in items]
            for k in range(0,x//weight+1):
                if k*weight <= j:
                    # print(temp)
                    list[i-1] = k
                    last_list = opt[i-1][j-k*weight][1]
                    res_list = [x + y for x, y in zip(list, last_list)]
                    # print(last_list)
                    temp += [[opt[i-1][j-k*weight][0]+k*value,res_list]]
                    # print("LAST:",opt[i-1][j-k*weight])
                    # print("K:",k," C:",copies)
            # print("LIST:",list)
            # print("TEMP:", temp)

            opt[i][j] = max(temp)

    return opt[i][j][0],opt[i][j][1]





# 1. Unbounded Knapsack
#
#    You have n items, each with weight w_i and value v_i, and has infinite copies.
#    **All numbers are positive integers.**
#    What's the best value for a bag of W?
#
best(3, [(2, 4), (3, 5)])
#    (5, [0, 1])
# print(best(3, [(2, 4, 2), (3, 5, 3)]))
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
# print(best(92, [(8, 9), (9, 10), (10, 12), (5, 6)]))
print(best(3, [(1, 5, 1), (1, 5, 3)]))
#    (15, [1, 2])
print('===============================')
print(best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)]))
#    (109, [1, 1, 7, 1])
#
#    Q: What are the time and space complexities?
#
#    filename: knapsack_unbounded.py
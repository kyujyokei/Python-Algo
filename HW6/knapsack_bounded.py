def best(x, items):
    sum = []
    list = []
    n = len(items)
    opt = [[0 for i in range(0,x+1)] for j in range(0,n+1)]
    # print(opt)
    items.insert(0,(0,0,0))

    for i in range(1, n+1):
        weight, value, copies = items[i][0],items[i][1], items[i][2]
        list += [0]
        for j in range(1,x+1):
            temp = []
            for k in range(0,x//weight+1):
                if k*weight <= j:
                    temp.append(opt[i-1][j-k*weight]+k*value)
            opt[i][j] = max(temp)


    print(opt)
    return opt[i][j]




#    Bounded Knapsack
#
#    You have n items, each with weight w_i and value v_i, and has c_i copies.
#    **All numbers are positive integers.**
#    What's the best value for a bag of W?
#
print(best(6, [(2, 4, 2), (3, 5, 10)]))
#    (5, [0, 1])
#
#    the input to the best() function is W and a list of triples (w_i, v_i, c_i).
#
#    tie-breaking: same as in p1:
#
#    >>> best(3, [(1, 5, 2), (1, 5, 3)])
#    (15, [2, 1])
#
#    >>> best(3, [(1, 5, 1), (1, 5, 3)])
#    (15, [1, 2])
#
#    >>> best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)])
#    (130, [6, 4, 1])
#
#    >>> best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)])
#    (236, [6, 7, 3, 7, 2])
#
#    Q: What are the time and space complexities?
#
#    filename: knapsack_bounded.py
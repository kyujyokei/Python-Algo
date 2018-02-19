def best_top(x, items):
    sum = []
    n = len(items)
    number_of_items = len(items) - 1
    list = [0 for i in items]
    opt = [[[0, 0] for i in range(0, x + 1)] for j in range(0, n + 1)]

    def _best(x, i):

        if i < 0: return 0
        if x == 0: return 0
        weight, value, copies = items[i][0],items[i][1],items[i][2]
        temp = []
        for j in range(0, x//weight + 1):
            max_c = min(j, copies)
            temp += [_best(x-(max_c*weight),i-1)+max_c*value]
        opt[i][j] = max(temp)
        return opt[i][j]

    res = _best(x, number_of_items)

    return res





def best_bottom(x, items):
    n = len(items)
    items.insert(0, (0, 0, 0))
    opt = [[[0,0] for i in range(0,x+1)] for j in range(0,n+1)]

    for i in range(1, n+1):
        weight, value, copies = items[i][0],items[i][1], items[i][2]
        for j in range(1,x+1):
            temp = []
            list = [0 for a in items]
            for k in range(0,x//weight+1):
                if k*weight <= j:
                    max_c = min(k,copies)
                    list[i-1] = max_c
                    temp += [[opt[i-1][j-max_c*weight][0]+max_c*value,max_c]]
            temp.sort(key=lambda x: (-x[0], x[1]))
            opt[i][j] = temp[0]
    def solution():
        temp_x = x
        # n = len(items) -1
        res = [0 for a in range(len(items)-1)]
        for i in range(n-1,-1,-1):
            res[i] = opt[i+1][temp_x][1]
            temp_x -= items[i+1][0]*res[i]

        return res
    # print(opt)
    return opt[i][j][0],solution()





def best(x, items):
    n = len(items)
    items.insert(0, (0, 0, 0))
    opt = [[[0,0] for i in range(0,x+1)] for j in range(0,n+1)]

    for i in range(1, n+1):
        weight, value, copies = items[i][0],items[i][1], items[i][2]
        for j in range(1,x+1):
            for k in range(0,min(copies,x//weight)+1):
                if j >= k*weight and opt[i][j][0] < opt[i-1][j-k*weight][0] + k * value:
                    # print(opt[i-1][j-k*weight])
                    opt[i][j] = [opt[i-1][j-k*weight][0] + k * value,k]

    def solution():
        temp_x = x
        # n = len(items) -1
        res = [0 for a in range(len(items)-1)]
        for i in range(n-1,-1,-1):
            res[i] = opt[i+1][temp_x][1]
            temp_x -= items[i+1][0]*res[i]

        return res
    # print(opt)
    return opt[i][j][0],solution()

#    Bounded Knapsack
#
#    You have n items, each with weight w_i and value v_i, and has c_i copies.
#    **All numbers are positive integers.**
#    What's the best value for a bag of W?
#
# print(best(5, [(2, 4, 2), (3, 5, 10)]))
#    (5, [0, 1])
#
#    the input to the best() function is W and a list of triples (w_i, v_i, c_i).
#
#    tie-breaking: same as in p1:
# print('===============================')
print(best(3, [(1, 5, 2), (1, 5, 3)]))
#    (15, [2, 1])
# print('===============================')
# print(best(3, [(1, 5, 1), (1, 5, 3)]))
#    (15, [1, 2])
# print('===============================')
# print(best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)]))
#    (130, [6, 4, 1])
# print('===============================')
print(best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)]))
#    (236, [6, 7, 3, 7, 2])
#
#    Q: What are the time and space complexities?
#
#    filename: knapsack_bounded.py
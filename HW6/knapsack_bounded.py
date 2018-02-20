def best_top(x, items):
    back = {}
    for i in range(0, len(items)):  back[i] = {}
    bounded = {}
    for i in range(0, len(items)+1):
        bounded[i] = {}
        bounded[i][0] = 0
    for i in range(0, x+1): bounded[0][i] = 0

    def _best(x, i):
        if x not in bounded[i+1]:
            max_v = 0
            w = items[i][0]
            count = min(items[i][2], x//w)
            for j in range(0, count+1):
                v = _best(x - j*w, i-1)
                if v + items[i][1]*j > max_v:
                    max_v = v + items[i][1]*j
                    back[i][x] = j
            bounded[i+1][x] = max_v
            print(bounded)
        return bounded[i+1][x]

    return _best(x, len(items)-1)





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
# print(best(3, [(1, 5, 2), (1, 5, 3)]))
#    (15, [2, 1])
# print('===============================')
print(best_top(3, [(1, 5, 1), (1, 5, 3)]))
#    (15, [1, 2])
# print('===============================')
# print(best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)]))
#    (130, [6, 4, 1])
# print('===============================')
# print(best_top(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)]))
#    (236, [6, 7, 3, 7, 2])
#
#    Q: What are the time and space complexities?
#
#    filename: knapsack_bounded.py
def max_wis(list):
    l = len(list)
    res_max = {-1:0, 0:0}
    res_list = {-1:[],0:[]}

    def _max_wis(n, list):

        if n not in res_max:
            b = _max_wis(n - 2, list[:n-2]) + list[n-1]
            c = _max_wis(n - 1, list[:n-1])
            if b >= c:
                res_max[n] = b
                res_list[n] = res_list[n-2] + [list[n-1]]
            else:
                res_max[n] = c
                res_list[n] = res_list[n-1]
        return res_max[n]

    max_val = _max_wis(l,list)
    max_list = res_list[l]

    return max_val, max_list

# res = {}
# res['a'] = 8
# print(res['a'])


# def fib(a,l):
#     total = 0
#     numList = []
#     i = l
#     while i > 0:
#         if a[i] >= 0:
#             total += a[i]
#             numList.append(a[i])
#             i -= 2
#         else:
#             i -= 1
#
#     return total, numList


print(max_wis([7,8,5]))
   # (12, [7,5])

print(max_wis([-1,8,10,-1,-9,-10,-11]))
   # (10, [10])

print(max_wis([]))
   # (0, [])
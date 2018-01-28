import random
import copy

def find (a, var, num):
    a[:] = [x - var for x in a]
    temp = copy.deepcopy(a)
    temp[:] = [abs(x) for x in temp]
    r = qselect(num, temp)
    res = [x for x in a[:] if abs(x) <= abs(r)]
    res[:] = [x + var for x in res]
    return res[:num]


def qselect(idx, a):
    if a == [] or idx > len(a) or idx < 1 :
        return []
    else:
        r = random.randint(0,len(a)-1)
        a[0], a[r]  = a[r], a[0]
        pivot = a[0]
        left = [x for x in a if x < pivot]
        l_len = len(left)

        if idx == l_len + 1:
            return pivot
        elif idx < l_len + 1:
            return qselect(idx, left)
        else:
            right = [x for x in a[1:] if x >= pivot]
            return qselect(idx-l_len-1, right)





# Given an array A of n numbers, a query x, and a number k,
#    find the k numbers in A that are closest (in value) to x.
#    For example:
#
#    find([4,1,3,2,7,4], 5.2, 2)	returns   [4,4]
#    find([4,1,3,2,7,4], 6.5, 3)	returns   [4,7,4]
#    find([5,3,4,1,6,3], 3.5, 2)	returns   [3,4]
#
print(find([4,1,3,2,7,4], 5.2, 2))
print(find([4,1,3,2,7,4], 6.5, 3))
print(find([5,3,4,1,6,3], 3.5, 2))
# print()
#
#    Filename: closest_unsorted.py
#    Must run in O(n) time.
#    The elements in the returned list must be in the original order.
#    In case two numbers are equally close to x, choose the earlier one.
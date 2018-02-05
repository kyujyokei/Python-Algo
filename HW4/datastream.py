import heapq
import random

def ksmallest(k,a):
    if k >= len(a):
        # a.sort()
        return sort(a)
    if a == [] or len(a) == 1:
        return a
    a = [x * -1 for x in a] # O(n)
    heap = list(a[:k])
    b = list(a[k:]) # O(n) for this and the line above
    heapq.heapify(heap) # O(k)
    for x in b: # O(n)
        if x > heap[0]:
            heapq.heappushpop(heap, x) # O(logk)
    heap = [x * -1 for x in heap] # O(n)
    return sort(heap) # O(nlogn)

def sort(a):
    if a == []:
        return []
    else:
        # r = random.randint(0, len(a)-1)
        # a[r], a[0] = a[0], a[r]
        pivot = [x for x in a if x == a[0]]
        left = [x for x in a if x < a[0]]
        right = [x for x in a[1:] if x > a[0]]
        return sort(left) + pivot + sort(right)

# Find the k smallest numbers in a data stream of length n (k<<n),
# using only O(k) space (the stream itself might be too big to fit in memory).
#
# print(ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7]))
# print(sort([10,7,23,2,9,3,7,8,11,5,7]))
# print(ksmallest(20,[10,7,23,2,9,3,7,8,11,5,7]))
# print(ksmallest(4,[2,2,2,2,2]))
# [2, 3, 5, 7]
# print(ksmallest(3, range(1000000, 0, -1)))
# [1, 2, 3]
#
# Note:
# a) it should work with both lists and lazy lists
# b) the output list should be sorted
#
# Q: What is your complexity? Write down the detailed analysis in report.txt.

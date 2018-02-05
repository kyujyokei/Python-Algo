import heapq

def kmerge(a, x):
    heap = []
    # split(a, x, heap)

# def mergesort(lst):
#     l = len(lst)
#     if l <= 1:
#         return lst
#     return mergesorted(mergesort(lst[:l//2]), mergesort(lst[l//2:]))
#
# def mergesorted(a, b):
#     i, j = 0, 0
#     la, lb = len(a), len(b)
#     while i < la or j < lb:
#         if i == la or (j != lb and a[i] > b[j]):
#             yield b[j]
#             j += 1
#         else:
#             yield a[i]
#             i += 1

def split(a, sec):

    if len(a) == 1 or a == []:
        return(a)

    avg = len(a)/float(sec)
    out = []
    heap = []
    temp = []
    last = 0.0
    # print("AVG:",avg)

    while last < len(a):
        out.append(a[int(last):int(last + avg)])
        # print(last, avg)
        last += avg

    for x in out:
        split(x, sec)
        if x != []:
            heapq.heappush(heap,x)
            print("heap:", heap)
            # heapq.heapify(heap)
            temp heapq.heappop(heap)
            print("heap:",heap)
            print("tem1:", temp, "\n")
    # print("temp:",temp)

    # print(heap)
    return temp

    # print("OUT:",out)
    # return split(out, sec)


print(split([5,3,4,4,8,2,6,4,9],3))

# 2. k-way mergesort (the classical mergesort is a special case where k=2).
#
#    >>> kmergesort([4,1,5,2,6,3,7,0], 3)
#    [0,1,2,3,4,5,6,7]
#
#    Q: What is the complexity? Write down the detailed analysis in report.txt.
#
#    Filename: kmergesort.py

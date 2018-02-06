import heapq

def split(a, k):
    if len(a) == 1 or a == []:
        return(a)
    avg = len(a)/float(k)
    out = []
    temp = []
    last = 0.0

    while last < len(a):
        out.append(a[int(last):int(last + avg)])
        last += avg

    for x in out:
        temp.append(merge(split(x, k),k))
    res = merge(temp, k)
    return res



def merge(a, k):
    if a == None or len(a) <= 1:
        return [a]

    else:
        pq = []
        heap = []
        ptr = []
        for i in range(0, len(a)):
            # print("A",a)
            # print(a[i][0])
            # if a[i] is int:
            #     heapq.heappush(heap, [a[i], 0, i])
            # else:
            #     print("A[i]",a[i])
            heapq.heappush(heap, [a[i][0], 0, i])
            # print("FIRST:", heap)
            ptr += [[0]]

            # print("TEMP:",temp)

        while heap != []:
            min_v = heapq.heappop(heap)
            var, idx, list_idx = min_v
            # print("MIN:",min_v, "\n")
            pq.append(var)
            # ptr[list_idx] += 1
            if idx < len(a[list_idx]) - 1:
                heapq.heappush(heap,[a[list_idx][idx+1],idx+1,list_idx])
            # print("HEAP:", heap)

        # print("---------pq---------",pq)
        return pq

    # print("OUT:",out)
    # return split(out, sec)


print(split([5,3,4,10,8,2,6,11,9],5))

# 2. k-way mergesort (the classical mergesort is a special case where k=2).
#
#    >>> kmergesort([4,1,5,2,6,3,7,0], 3)
#    [0,1,2,3,4,5,6,7]
#
#    Q: What is the complexity? Write down the detailed analysis in report.txt.
#
#    Filename: kmergesort.py

def mergesort(lst):
    l = len(lst)
    if l <= 1:
        return lst
    return mergesorted(mergesort(lst[:l//2]), mergesort(lst[l//2:]))

def mergesorted(a, b):
    i, j = 0, 0
    la, lb = len(a), len(b)
    while i < la or j < lb:
        if i == la or (j != lb and a[i] > b[j]):
            yield b[j]
            j += 1
        else:
            yield a[i]
            i += 1




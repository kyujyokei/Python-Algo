def mergesort(a):
    if len(a) <= 1 : return a
    else:
        mid = len(a)//2
        left = a[:mid]
        right = a[mid:]

        mergesort(left)
        mergesort(right)

        i, j, k, = 0, 0, 0
        # print(a)
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                a[k] = right[j]
                j += 1
            else:
                a[k] = left[i]
                i += 1
            k += 1

        while i < len(left):
            a[k] = left[i]
            k += 1
            i += 1

        while j > len(right):
            a[k] = right[j]
            k += 1
            j += 1
    return a


# print(mergesort([5,4,6,9,8,7,2,3]))

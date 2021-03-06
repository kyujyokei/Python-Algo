def mergesort(a, m):
    if len(a) <= 1 : return 0
    else:
        mid = len(a)//2
        left = a[:mid]
        right = a[mid:]

        m += mergesort(left, m) + mergesort(right, m)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                a[k] = right[j]
                j += 1
                m = m + (len(left) - i)

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
    return m


def num_inversions(a):
    return mergesort(a, 0)


print(num_inversions([4,1,3,2]))
print(num_inversions([2,4,1,3]))
print(num_inversions([4,3,2,1]))

# print(num_inversions([4, 1, 3, 2]))
# print(num_inversions([2, 4, 1, 3]))
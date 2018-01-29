def find(a):
    list = []
    a.sort()
    # print(a)

    # print(left, right)
    for i in a:
        left = 0
        right = len(a) - 1
        while left < right:
            # print("L: ",a[left]," ,R: ",a[right]," ,i: ", i)
            if a[left] + a[right] < i:
                # print("BIG",a[left],a[right],a[i])
                left += 1
                # print("LEFT +\n")
            elif a[left] + a[right] > i:
                # print("SMALL",a[left], a[right], a[i])
                right -= 1
                # print("RIGHT -\n")

            else:
                # print("EQUAL", a[left], a[right], i)
                list.append([a[left], a[right], i])
                left += 1
                right -= 1

    return list

print(find([1, 4, 2, 3, 5]))
# returns[(1, 3, 4), (1, 2, 3), (1, 4, 5), (2, 3, 5)]
#
# Filename: xyz.py
# Must run in O(n ^ 2) time.

import bisect

def find(a, x, range):
    list = []
    right = bisect.bisect(a, x)
    left = right - 1
    print("left: ", left, " right: ", right)
    while range > len(list):
        if abs(x - a[left]) > abs(x - a[right]):
            list.append(a[right])
            if right + 1 == len(a):
                while range > len(list):
                    list.insert(0, a[left])
                    left -= 1
            else:
                right += 1
        else:
            list.insert(0, a[left])
            if left == 0:
                while range > len(list):
                    list.append(a[right])
                    right += 1
            else:
                left -= 1
    return list

a = find([1, 2, 3, 4, 4, 7], 5.2, 2)
print(a)
#     # returns[4, 4]
b = find([1, 2, 3, 4, 4, 7], 6.5, 3)
print(b)
# # returns[4, 4, 7]
#
c = find([1, 2, 3, 4, 4, 6, 6], 5, 3)
    # returns[4, 4, 6]
d = find([1, 2, 3, 4, 4, 5, 6], 4, 5)
print(c)
print(d)
#     # returns[2, 3, 4, 4, 5]
print(find([1,2,3,3,3,4,5], 0, 3))
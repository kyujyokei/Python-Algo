def sort(a):
    if a == []:
        return []
    else:
        pivot = a[0]
        left = [x for x in a if x < pivot ]
        right = [x for x in a[1:] if x >= pivot]
        return [sort(left)] + [pivot] + [sort(right)]

def sorted(tree):
    return [] if tree == [] else sorted(tree[0]) + [tree[1]] + sorted(tree[2])

def _search(tree, x):
    if tree == []:
        return tree
    else:
        # print(tree)
        mid = tree[1]
        left = tree[0]
        right = tree [2]

        if x == mid:
            return mid
        elif x < mid:
            return _search(left, x)
        else:
            return _search(right, x)

def search(tree, x):
    return _search(tree, x) != []

def insert(tree, x):
    node = _search(tree, x)
    if node == []:
        node.extend([[],x,[]])

tree1 = [[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[[], 6.5, []], 7, [[], 9, []]]]]

# a = search(tree1, 6.5)
# print(a)
# insert(tree1, 10)
# print(tree1)
# a = search(tree1, 10)
# print(a)
# sort(tree1)
print(sorted(tree1))
print(search(tree1, 6.5))
# This is O(nlogn) because...
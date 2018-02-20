import random

def qselect(idx, a):
    if a == [] or idx > len(a) or idx < 1 :
        return []
    else:
        r = random.randint(0,len(a)-1)
        a[0], a[r] = a[r], a[0]
        pivot = a[0]
        left = [x for x in a if x < pivot]
        l_len = len(left)

        if idx == l_len + 1:
            return pivot
        elif idx < l_len + 1:
            return qselect(idx, left)
        else:
            right = [x for x in a[1:] if x >= pivot]
            return qselect(idx - l_len - 1, right)

print(qselect(6,[1,3,6,7,8,10,99]))
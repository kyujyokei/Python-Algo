def longest(a):
    height, max = search(a)
    return max

def search(a):
    if a == []: return 0, 0
    l_hei, l_max = search(a[0])
    r_hei, r_max = search(a[2])
    c_max = l_max if l_max > r_max else r_max
    c_height = l_hei if l_hei > r_hei else r_hei
    max = (l_hei + r_hei) if (l_hei + r_hei) > c_max else c_max
    return c_height+1, max

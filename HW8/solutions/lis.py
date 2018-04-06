__author__ = "Zhang, He"

from collections import defaultdict


def lis(s):
    a = ["-inf"] + list(s) + ["inf"]
    n = len(a)
    d = defaultdict(int)
    back = defaultdict(lambda: -1)
    trackmax, indexmax = 0, 0
    for j in range(1, n):
        for k in range(j):
            if a[k] < a[j] or a[j] == "inf":
                temp = d[k] + 1
            if temp > d[j]:
                d[j] = temp
                back[j] = k
        if j < n - 1 and d[j] > trackmax:
            trackmax = d[j]
            indexmax = j
    return solution(indexmax, a, back)


def solution(i, a, back):
    if i < 1:
        return ""
    return solution(back[i], a, back) + str(a[i])


if __name__ == "__main__":
    print(lis("aebbcg"))
    print(lis("zyx"))
    print(lis("1234567890"))


__author__ = "Liang Huang"

from collections import defaultdict

def lis(s):
    def solution(i):
        return "" if i<0 else solution(back[i]) + chr(a[i]) # int to char

    a = list(map(ord, s)) + [float("inf")] # convert chars to ints
    print("A",a)
    d = defaultdict(int)
    back = defaultdict(lambda :- 1)
    for j, cj in enumerate(a):
        for k, ck in enumerate(a[:j]):
            if ck < cj and d[k] + 1 > d[j]:
                d[j] = d[k] + 1
                back[j] = k
    return solution(back[len(a)-1]) # exclude the final padding

if __name__=="__main__":
    print(lis("aebbcg"))
    print(lis("zyx"))
    print(lis("1234567890"))
    print(lis("x"))
    print(lis(""))
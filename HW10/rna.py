
def best(n):

    res = {}
    l = 0
    r = len(n)
    d = {'A':[0,'.'], 'U':[0,'.'], 'C':[0,'.'], 'G':[0,'.'], 'AU':[1,'()'], 'GC':[1,'()'], 'GU':[1,'()'], 'UA':[1,'()'], 'CG':[1,'()'], 'UG':[1,'()']}

    def pair(a):
        rna = set(['AU', 'GC', 'GU', 'UA', 'CG', 'UG'])
        return a in rna

    def find(n):

        if len(n) == 1:
            return 0, '.'
        elif len(n) == 0:
            return 0, ''
        i, j = 0, len(n)
        if pair(n[i] + n[j-1]): # if they make a pair
            sum, path = find(n[i+1:j-1])
            return sum + 1, '(' + path + ')'
        else:
            temp = []
            for k in range(1,j):
                sum1, path1 = find(n[0:k])
                sum2, path2 = find(n[k:j])
                temp.append([sum1+sum2, path1+path2])
            # print(temp)
            return max(temp, key= lambda x: x[0])

    print(dict(res))
    def solution(lis):
        s = ''
        for i in range(0,len(lis)):
            s += lis[i]
        return s

    return find(n, l, r), solution(res)

def total():
    return 0

def kbest():
    return 0


print(best('GCACG'))
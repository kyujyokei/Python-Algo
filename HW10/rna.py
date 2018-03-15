def best(n):

    def find(n):

        if len(n) <= 1: return 0
        i, j = 0, len(n)
        # print("N:",n)
        if pair(n[i] + n[j-1]): # if they make a pair
            return find(n[i+1:j-1]) + 1
        else:
            temp = []
            for k in range(1,j):
                # print(n[0:k],n[k:j])
                temp += [find(n[0:k]) + find(n[k:j])]
            return max(temp)

    return find(n)


def pair (a):
    rna = set(['AU','GC','GU','UA','CG','UG'])
    return a in rna

# a = 'A'
# b = 'B'
# print(pair(a+b))
print(best('GUUAGAGUCU'))
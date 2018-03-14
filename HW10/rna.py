def best(n):


    if pair(n[0] + n[-1]):
        print('bui')

    return 0


def pair (a):
    rna = set(['AU','GC','GU','UA','CG','UG'])
    return a in rna

a = 'A'
b = 'B'
print(pair(a+b))
print(best('ACAGU'))
def bsts(n):
    res = {0:1,1:1}

    def _bsts(n):
        if n not in res:
            sum = 0
            for i in range(1,n+1):
                sum += _bsts(i-1) * _bsts(n-i)
            res[n] = sum
        return res[n]
    _bsts(n)


    return res[n]

print(bsts(1))
print(bsts(2))
print(bsts(3))
print(bsts(4))
print(bsts(5))
print(bsts(6))
print(bsts(7))
print(bsts(8))
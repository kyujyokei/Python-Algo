def num_no(n):
    return _num(n)

def num_yes(n):
    return (2**n) - _num(n)

def _num(n):
    res = {-1:1,0:1}
    def _fib(n):
        if n not in res:
            res[n] = _fib(n-2) + _fib(n-1)
        return res[n]
    _fib(n)
    return res[n]

   # >>> num_no(3)
   # 5
   # >>> num_yes(3)
   # 3

print(num_no(5))
print(num_yes(5))
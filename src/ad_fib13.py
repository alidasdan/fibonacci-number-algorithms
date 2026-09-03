#!/usr/bin/env python3

# author: ali dasdan

from ad_util import negafib, fib_test

# compute the nth fibonacci number using an integer formula in
# https://blog.paulhankin.net/fibonacci/ . the formula
# (4 << m*(3+m)) // ((4 << 2*m) - (2 << m) - 1) & ((2 << m) - 1)
# produces the sequence 0, 1, 2, 3, 5, 8, ..., i.e., it returns
# F[m+1], so it is evaluated at m = n - 1 to return F[n]. n <= 1 is
# handled directly since the formula does not cover it.
def fib(n:int) -> int:
    n0, n = n, abs(n)
    if n <= 1:
        r = n
    else:
        m = n - 1
        num = (4 << m * (3 + m))
        denom = ((4 << 2 * m) - (2 << m) - 1)
        mod = ((2 << m) - 1)
        r = (num // denom) & mod
    if n0 < 0:
        return negafib(n, r)
    return r

def main():
    hi = 10
    for n in range(hi):
        assert fib(n) == fib_test(n)

    print('success')

if __name__ == '__main__':
    main()

# EOF

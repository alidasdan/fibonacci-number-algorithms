#!/usr/bin/env python3

# author: ali dasdan

from ad_util import negafib, fib_test

# compute the nth fibonacci number using an integer formula in
# https://blog.paulhankin.net/fibonacci/ . The sequence is 0, 1, 2, 3,
# 5, 8, ..., i.e., correct after 2. the formula is: (4 << n*(3+n)) //
# ((4 << 2*n) - (2 << n) - 1) & ((2 << n) - 1)
def fib(n:int) -> int:
    n0, n = n, abs(n)
    num = (4 << n * (3 + n))
    denom = ((4 << 2 * n) - (2 << n) - 1)
    mod = ((2 << n) - 1)
    r = (num // denom) & mod
    if n0 < 0:
        return negafib(n, r)
    return r

def main():
    hi = 10
    for n in range(1, hi):
        # need to use n + 1 on the RHS below due to the sequence not
        # starting with 0, 1, 1, 2, ...
        assert fib(n) == fib_test(n + 1)

    print('success')

if __name__ == '__main__':
    main()

# EOF

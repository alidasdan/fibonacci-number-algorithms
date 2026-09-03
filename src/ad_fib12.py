#!/usr/bin/env python3

# author: ali dasdan

import math
from ad_util import negafib, fib_test

# iteratively compute the nth fibonacci number using the formula
# F[n] = round(phi * F[n-1]), valid for n >= 3. it is formula 64 in
# vajda and formula 73 in dunlap; see r. knott's fibonacci and golden
# ratio formulae. this is exact only up to n = 78; past that the
# rounding error accumulated over the iterations takes over.
def fib(n:int) -> int:
    n0, n = n, abs(n)
    sqrt_5 = math.sqrt(5)
    phi = float(1 + sqrt_5) / 2
    if n == 0:
        r = 0
    elif n == 1:
        r = 1
    elif n == 2:
        r = 1
    else:
        r = 1
        for _ in range(3, n + 1):
            r = round(phi * r)
        r = int(r)
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

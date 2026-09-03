#!/usr/bin/env python3

# author: ali dasdan

import math
from ad_util import negafib, fib_test

# compute the nth fibonacci number using golden ratio based closed
# formula and rounding: F[n] = round(phi^n / sqrt(5)). this is exact
# only up to n = 70; past that the floating-point precision runs out,
# and past n = 1474 math.pow overflows and raises, which the caller
# reports.
def fib(n:int) -> int:
    n0, n = n, abs(n)
    if n == 0:
        r = 0
    elif n == 1:
        r = 1
    else:
        sqrt_5 = math.sqrt(5)
        phi = float(1 + sqrt_5) / 2
        phi_n = math.pow(phi, n)
        r = round(phi_n / sqrt_5)
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

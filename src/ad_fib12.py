#!/usr/bin/env python3

# author: ali dasdan

import math
from ad_util import negafib, fib_test, at_exit

# iteratively compute the nth fibonacci number using this formula (no
# reference found in the literature yet): F[n] = round(phi * F[n-1]).
def fib(n:int) -> int:
    n0, n = n, abs(n)
    try:
        sqrt_5 = math.sqrt(5)
    except Exception as err:
        at_exit(err)
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

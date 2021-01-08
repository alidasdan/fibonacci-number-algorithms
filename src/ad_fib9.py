#!/usr/bin/env python3

# author: ali dasdan

from typing import List
from ad_util import negafib, fib_test

# recursively compute the nth fibonacci number using the following
# formula: F[2k]=F[k]*[2*F[k+1]-F[k]] and F[2k+1]=F[k+1]^2+F[k]^2.
def fib_recur(n:int, F:List[int]) -> List[int]:
    if F[n] is None:
        if n <= 0:
            F[n] = 0
        elif n == 1:
            F[n] = 1
        elif n == 2:
            F[n] = 1
        else:
            k = n >> 1
            f1 = fib_recur(k, F)
            f2 = fib_recur(k + 1, F)
            if n % 2 == 0:
                F[n] = 2 * f1 * f2 - f1 * f1
            else:
                F[n] = f2 * f2 + f1 * f1
    return F[n]

def fib(n:int) -> int:
    n0, n = n, abs(n)
    r = fib_recur(n, [None] * (n + 1))
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

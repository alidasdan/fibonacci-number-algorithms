#!/usr/bin/env python3

# author: ali dasdan

from math import sqrt, pow
from ad_util import negafib, fib_test, at_exit

# compute the nth fibonacci number using the formula presented at
# https://orlp.net/blog/magical-fibonacci-formulae/.
def fib(n:int) -> int:
    n0, n = n, abs(n)
    if n == 0:
        r = 0
    elif n == 1:
        r = 1
    else:
        r = (b := 2<<n)**n * b // (b * b - b - 1) % b
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

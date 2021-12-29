#!/usr/bin/env python3

# author: ali dasdan

from ad_util import negafib, fib_test

# compute the nth fibonacci number with help of Lucas numbers: e_n =
# (e_{n-1} + 5f_{n-1})/2; f_n = (e_{n-1}+f_{n-1})/2
def fib(n:int) -> int:
    n0, n = n, abs(n)
    e, f = 2, 0
    for _ in range(n):
        e, f = (e + 5 * f) // 2, (e + f) // 2
    r = f
    if n0 < 0:
        return negafib(n, r)
    return r

def main():
    hi = 10
    for n in range(1, hi):
        assert fib(n) == fib_test(n)

    print('success')

if __name__ == '__main__':
    main()

# EOF

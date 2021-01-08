#!/usr/bin/env python3

# author: ali dasdan

from ad_util import negafib, fib_test

# compute the nth fibonacci number using recursion w/o memoization
# F[0]=0; F[1]=1; F[n]=F[n-1]+F[n-2].
def fib_recur(n:int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recur(n - 1) + fib_recur(n - 2)

def fib(n:int) -> int:
    n0, n = n, abs(n)
    r = fib_recur(n)
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

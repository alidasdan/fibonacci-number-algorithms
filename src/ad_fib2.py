#!/usr/bin/env python3

# author: ali dasdan

from ad_util import negafib, fib_test

# compute the nth fibonacci number using recursion w/ memoization:
# F[0]=0; F[1]=1; F[n]=F[n-1]+F[n-2].
def fib_recur(n, F):
    if F[n] is None:
        if n == 0:
            F[n] = 0
        elif n == 1:
            F[n] = 1
        else:
            F[n] = fib_recur(n - 1, F) + fib_recur(n - 2, F)
    return F[n]

def fib(n):
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

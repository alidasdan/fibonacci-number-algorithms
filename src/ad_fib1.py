#!/usr/bin/python

# author: ali dasdan

import sys
from ad_util import *

# compute the nth fibonacci number using recursion w/o memoization
# F[0]=0; F[1]=1; F[n]=F[n-1]+F[n-2].
def fib_recur(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n - 1) + fib_recur(n - 2)

def fib(n):
    n0, n = n, abs(n)
    r = fib_recur(n)
    if n0 < 0:
        return negafib(n, r)
    return r

def main():
    hi = 10
    for n in range(hi):
        assert fib(n) == fib_test(n)

    print 'success'

if __name__ == '__main__':
    main()

# EOF

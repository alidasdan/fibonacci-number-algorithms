#!/usr/bin/python

# author: ali dasdan

import sys
from ad_util import *

# compute the nth fibonacci number using the 2x2 matrix based formula
# iteratively: [[1,1], [1,0]]^n = [[F[n+1],F[n]], [F[n],F[n-1]]].
def fib(n):
    n0, n = n, abs(n)
    if n == 0:
        r = 0
    else:
        m = [[1, 0], [0, 1]]
        for i in range(1, n):
            #m = mat_mul(m, [[1, 1], [1, 0]])
            m = mat_mul_opt(m)
        r = m[0][0]
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

#!/usr/bin/python

# author: ali dasdan

import sys
import math
from ad_util import *

# compute the nth fibonacci number using golden ratio based closed
# formula and rounding: F[n] = round(phi^n / sqrt(5)).
def fib(n):
    n0, n = n, abs(n)
    if n == 0:
        r = 0
    elif n == 1:
        r = 1
    else:
        try:
            sqrt_5 = math.sqrt(5)
        except Exception, msg:
            at_exit(msg)
        phi = float(1 + sqrt_5) / 2
        #phi_n = num_pow_iter(phi, n)
        try:
            phi_n = math.pow(phi, n)
        except Exception, msg:
            at_exit(msg)
        r = round(phi_n / sqrt_5)
        r = long(r)
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

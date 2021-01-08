#!/usr/bin/env python3

# author: ali dasdan

from math import sqrt, pow
from ad_util import negafib, fib_test, at_exit

# compute the nth fibonacci number using golden ratio based closed
# formula and rounding: F[n] = round(phi^n / sqrt(5)).
def fib(n:int) -> int:
    n0, n = n, abs(n)
    if n == 0:
        r = 0
    elif n == 1:
        r = 1
    else:
        try:
            sqrt_5 = sqrt(5)
        except Exception as err:
            at_exit(err)
        phi = float(1 + sqrt_5) / 2
        #phi_n = num_pow_iter(phi, n)
        try:
            phi_n = pow(phi, n)
        except Exception as err:
            at_exit(err)
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

#!/usr/bin/env python3

# author: ali dasdan

from ad_util import negafib, fib_test

# compute the nth fibonacci number using iteration in constant space
# F[0]=0; F[1]=1; F[n]=F[n-1]+F[n-2].
def fib(n):
    n0, n = n, abs(n)
    if n == 0:
        r = 0
    elif n == 1:
        r = 1
    else:
        f2, f1 = 1, 0
        for _ in range(2, n + 1):
            f2, f1 = f2 + f1, f2
        r = f2
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

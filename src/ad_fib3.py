#!/usr/bin/env python3

# author: ali dasdan

from ad_util import negafib

# compute the nth fibonacci number using iteration in constant space
# F[0]=0; F[1]=1; F[n]=F[n-1]+F[n-2].
def fib(n:int) -> int:
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
    # this is the same algorithm as the fib_test oracle in ad_util, so
    # checking it against that oracle would prove nothing. it is
    # checked against published values instead.
    for (n, fn) in enumerate([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]):
        assert fib(n) == fn

    assert fib(100) == 354224848179261915075
    assert fib(-10) == -55
    assert fib(-11) == 89

    print('success')

if __name__ == '__main__':
    main()

# EOF

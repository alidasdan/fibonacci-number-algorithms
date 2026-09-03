#!/usr/bin/env python3

# author: ali dasdan

from ad_util import is_even, negafib, fib_test

# the base values the fill loop below starts from.
BASE = {0: 0, 1: 1, 2: 1}

# iteratively compute the nth fibonacci number using the following
# formula: F[2k]=F[k]*[2*F[k+1]-F[k]] and F[2k+1]=F[k+1]^2+F[k]^2.
def fib(n:int) -> int:
    n0, n = n, abs(n)

    # find indexes that need F values. None marks an index whose value
    # is not known yet.
    F = {n: None}
    qinx = [n]   # queue of indexes
    while qinx:
        k = qinx.pop() >> 1
        for j in (k, k + 1):
            if j not in F:
                F[j] = None
                qinx.append(j)

    # set base values
    F.update(BASE)

    # fill the indexes that need values. the increasing index order
    # guarantees that F[k >> 1] and F[(k >> 1) + 1] are already known.
    for k in sorted(F.keys()):
        if k in BASE:
            continue
        k2 = k >> 1
        f1, f2 = F[k2], F[k2 + 1]
        if is_even(k):
            F[k] = 2 * f2 * f1 - f1 * f1
        else:
            F[k] = f2 * f2 + f1 * f1

    r = F[n]
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

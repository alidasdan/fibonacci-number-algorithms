#!/usr/bin/env python3

# author: ali dasdan

from ad_util import negafib, fib_test

# iteratively compute the nth fibonacci number using the following
# formula: F[2k]=F[k]*[2*F[k+1]-F[k]] and F[2k+1]=F[k+1]^2+F[k]^2.
def fib(n:int) -> int:
    n0, n = n, abs(n)
    F = {}

    # find indexes that need F values
    qinx = []   # queue of indexes
    qinx.append(n)
    F[n] = -1   # -1 to mark such values
    while qinx:
        k = qinx.pop() >> 1
        if k not in F:
            F[k] = -1
            qinx.append(k)
        if (k + 1) not in F:
            F[k + 1] = -1
            qinx.append(k + 1)

    # set base values
    F[0], F[1], F[2] = 0, 1, 1

    # fill the indexes that need values
    keys_sorted = sorted(F.keys())
    for k in keys_sorted[3:]:
        k2 = k >> 1
        f1, f2 = F[k2], F[k2 + 1]
        if k % 2 == 0:
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

#!/usr/bin/env python3

import sys
from typing import List

Matrix = List[List[int]]

def show_usage(usage:str) -> None:
    print("Usage:" + sys.argv[0] + usage)

def at_exit(msg:str, kind:str='Error', usage:str='') -> None:
    if msg != "" and msg is not None:
        print(kind + ":", "'" + str(msg) + "'")
    if usage != '':
        show_usage(usage)
    sys.exit(0)

# check if n is odd or even
def is_odd(n:int) -> int:
    return n & 1

def is_even(n:int) -> int:
    return not is_odd(n)

# given the nth fibonacci number, return the corresponding
# negafibonacci number.
def negafib(n:int, Fn:List[int]) -> List[int]:
    if is_odd(n + 1):
        return -Fn
    return Fn

# compute a^n for scalar a.
def num_pow_iter(a:int, n:int) -> int:
    n_bits = bin(n)[2:]
    r = 1
    for b in n_bits:
        r = r * r
        if b == '1':
            r *= a
    return r

# multiply 2x2 matrices m1 and m2 and return the product.
def mat_mul(m1:Matrix, m2:Matrix) -> Matrix:
    m = [[0, 0], [0, 0]]
    m[0][0] = m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]
    m[0][1] = m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]
    m[1][0] = m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]
    m[1][1] = m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]
    return m

# multiply 2x2 matrices m1 and m2 and return the product,
# where m2=[[1,1],[1,0]].
def mat_mul_opt(m1:Matrix) -> Matrix:
    m = [[0, 0], [0, 0]]
    m[0][0] = m1[0][0] + m1[0][1]
    m[0][1] = m1[0][0]
    m[1][0] = m1[1][0] + m1[1][1]
    m[1][1] = m1[1][0]
    return m

# compute m^n for 2x2 matrix m recursively.
def mat_pow_recur(m:Matrix, n:int) -> Matrix:
    r = [[1, 0], [0, 1]] # identity
    if n > 1:
        r = mat_pow_recur(m, n >> 1)
        r = mat_mul(r, r)
    if n % 2 == 1:
        r = mat_mul(r, m)
    return r

# compute m^n for 2x2 matrix m = [[1, 1], [1, 0]] recursively.
def mat_pow_opt_recur(n:int) -> Matrix:
    r = [[1, 0], [0, 1]] # identity
    if n > 1:
        r = mat_pow_opt_recur(n >> 1)
        r = mat_mul(r, r)
    if n % 2 == 1:
        r = mat_mul_opt(r)
    return r

# compute m^n for 2x2 matrix m iteratively.
def mat_pow_iter(m:Matrix, n:int) -> Matrix:
    n_bits = bin(n)[2:]
    r = [[1, 0], [0, 1]] # identity
    for b in n_bits:
        r = mat_mul(r, r)
        if b == '1':
            r = mat_mul(r, m)
    return r

# compute m^n for 2x2 matrix m = [[1, 1], [1, 0]] iteratively.
def mat_pow_opt_iter(n:int) -> Matrix:
    n_bits = bin(n)[2:]
    r = [[1, 0], [0, 1]] # identity
    for b in n_bits:
        r = mat_mul(r, r)
        if b == '1':
            r = mat_mul_opt(r)
    return r

# compute the nth Fibonacci number using the simple, linear time and
# constant space algorithm.
def fib_test(n:int) -> int:
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
        if n % 2 == 0:
            assert is_even(n)
        else:
            assert is_odd(n)

    for (n, fn) in enumerate([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]):
        assert fib_test(n) == fn

    for n in range(hi):
        fn = fib_test(n)
        if is_odd(n):
            assert negafib(n, fn) == fn
        else:
            assert negafib(n, fn) == -fn

    p = 1
    for n in range(hi):
        assert num_pow_iter(2, n) == p
        p = p << 1

    iden = [[1, 0], [0, 1]]
    mfib = [[1, 1], [1, 0]]

    m = mat_mul(iden, iden)
    assert m[0][0] == iden[0][0]
    assert m[0][1] == iden[0][1]
    assert m[1][0] == iden[1][0]
    assert m[1][1] == iden[1][1]

    m = mat_mul_opt(iden)
    assert m[0][0] == mfib[0][0]
    assert m[0][1] == mfib[0][1]
    assert m[1][0] == mfib[1][0]
    assert m[1][1] == mfib[1][1]

    m = mat_pow_recur(iden, hi)
    assert m[0][0] == iden[0][0]
    assert m[0][1] == iden[0][1]
    assert m[1][0] == iden[1][0]
    assert m[1][1] == iden[1][1]

    m = mat_pow_iter(iden, hi)
    assert m[0][0] == iden[0][0]
    assert m[0][1] == iden[0][1]
    assert m[1][0] == iden[1][0]
    assert m[1][1] == iden[1][1]

    m1 = mat_pow_recur(mfib, hi)
    m2 = mat_pow_opt_recur(hi)
    assert m1[0][0] == m2[0][0]
    assert m1[0][1] == m2[0][1]
    assert m1[1][0] == m2[1][0]
    assert m1[1][1] == m2[1][1]

    m1 = mat_pow_iter(mfib, hi)
    m2 = mat_pow_opt_iter(hi)
    assert m1[0][0] == m2[0][0]
    assert m1[0][1] == m2[0][1]
    assert m1[1][0] == m2[1][0]
    assert m1[1][1] == m2[1][1]

    print('success')

if __name__ == '__main__':
    main()

# EOF

#!/usr/bin/env python3

# author: ali dasdan

# cross-algorithm tests. each ad_fibN.py checks itself over n in
# [0, 9] only, and none of them checks a negative n even though they
# all implement the negafibonacci case. this program checks every
# algorithm against the fib_test oracle in ad_util over a much wider
# range, in both directions.
#
# the algorithms that use floating-point arithmetic are exact only up
# to a limit. those limits are recorded below and asserted exactly, so
# that a limit moving in either direction is reported as a failure
# rather than passing unnoticed: they are a property of the algorithms
# worth pinning down, not a defect.

import importlib
from typing import Dict, Optional

from ad_util import alg_ids, fib_test

N_HI = 200      # check n in [0, N_HI]
N_NEG_HI = 30   # check n in [-N_NEG_HI, -1]

# the largest n for which an algorithm still returns the exact F(n).
# an algorithm absent from this table is expected to be exact for
# every n checked here.
EXACT_UPTO: Dict[int, int] = {
    4: 70,   # binet's formula, closed form in floating point
    5: 70,   # binet's formula w/ rounding, closed form in floating point
    12: 78,  # F[n] = round(phi * F[n-1]), error accumulates over n rounds
}

# alg 1 is the exponential-time recursion w/o memoization, so it is
# checked over a small range only.
SLOW_ALGS: Dict[int, int] = {1: 25}

# return the smallest n in [0, hi] where mod.fib(n) differs from the
# oracle, or None if there is no such n.
def first_mismatch(mod, hi:int) -> Optional[int]:
    for n in range(hi + 1):
        if mod.fib(n) != fib_test(n):
            return n
    return None

def check_alg(alg_id:int) -> None:
    mod = importlib.import_module('ad_fib' + str(alg_id))
    hi = SLOW_ALGS.get(alg_id, N_HI)

    # the first mismatch must land exactly where the limit says.
    limit = EXACT_UPTO.get(alg_id)
    want = None if limit is None else limit + 1
    got = first_mismatch(mod, hi)
    assert got == want, \
        'alg %d: expected the first mismatch at %s, got %s' % (alg_id, want, got)

    # every algorithm is exact on the negative branch over this range.
    # the range is clamped to stay inside the range each algorithm is
    # checked over and inside its exact range, if it has one.
    neg_hi = min(hi, N_NEG_HI)
    if limit is not None:
        neg_hi = min(neg_hi, limit)
    for n in range(1, neg_hi + 1):
        assert mod.fib(-n) == fib_test(-n), \
            'alg %d: fib(%d) = %s, expected %s' % (alg_id, -n, mod.fib(-n), fib_test(-n))

def main():
    ids = alg_ids()
    assert len(ids) > 0, 'no ad_fibN.py files found'
    for alg_id in ids:
        check_alg(alg_id)

    print('success')

if __name__ == '__main__':
    main()

# EOF

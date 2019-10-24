#!/usr/bin/env python3

# compute fibonacci numbers using multiple algorithms. this is a good
# exercise in alg development, including recursion vs iteration,
# dynamic programming w/ or w/o memoization, closed formula vs
# iteration, floating point errors.

# author: ali dasdan

import sys
import getopt
import math
import importlib
from time import process_time

from ad_util import negafib, at_exit
import ad_fib3

# generate all fib numbers from 0th to the nth using the iterative
# linear-time algorithm.
def fib_all(n):
    n0, n = n, abs(n)
    if n == 0:
        F = [0]
    elif n == 1:
        F = [0, 1]
    else:
        F = []
        F.append(0)
        F.append(1)
        for i in range(2, n + 1):
            F.append(F[i - 1] + F[i - 2])
    if n0 < 0:
        for i in range(n + 1):
            F[i] = negafib(i, F[i])
    return F

### section: results production

# get conf interval
def get_confint(avr, std, n, is_pos=True, fmt_str='.6f'):
    k = 0.0
    if n > 0:
        try:
            k = 1.96 * math.sqrt(n)
        except Exception as err:
            at_exit(err)
    lo = avr - k * std
    if is_pos:
        lo = max(0.0, lo)
    hi = avr + k * std
    return format(lo, fmt_str), format(hi, fmt_str)

# compare results in absolute
def compare_abs(a, b, do_fmt=True, fmt_str='.6f'):
    if do_fmt:
        return format(a - b, fmt_str)
    return a - b

# compare results in relative
def compare_rel(a, b, do_fmt=True, fmt_str='.6f'):
    diff = compare_abs(a, b, False)
    if b == 0:
        if do_fmt:
            return format(a, fmt_str)
        return a
    if do_fmt:
        return format(float(abs(diff)) / b, fmt_str)
    return float(abs(diff)) / b

# run mod.fib(n) nrepeats times, also measure its runtime in seconds.
def run(mod, n, nrepeats):
    sum1 = 0.0
    sum2 = 0.0
    for _ in range(nrepeats):
        t_start = process_time()
        try:
            r = mod.fib(n)
        except Exception as err:
            at_exit(err)
        t = process_time() - t_start
        sum1 += t
        sum2 += t * t
    avr = float(sum1) / nrepeats
    try:
        std = math.sqrt(sum2 / nrepeats - avr * avr)
    except Exception as err:
        at_exit(err)
    return r, avr, std

### section: main

# generate all the fib numbers from the 1st to the nth
def gen_all_fib_nums_upto(n):
    start_all = process_time()
    h = fib_all(n)
    elapsed_all = process_time() - start_all
    print(h)
    print('time elapsed', elapsed_all)

# run the other requested algos with the given ids. the ids are used
# to construct the algo name, which in turn is used to construct the
# module name in runtime.
def run_requested_algos(n, alg_ids, nrepeats):
    results = []
    r_n = None
    for alg_id in alg_ids:
        alg_nm = 'ad_fib' + str(alg_id)
        mod = importlib.import_module(alg_nm, package=None)
        r_n, avr_n, std_n = run(mod, n, nrepeats)
        results.append((alg_id, r_n, avr_n, std_n))

    sorted_results = sorted(results, key=lambda x: x[2])
    return sorted_results

# compare and print the results in the increasing runtime order
def cmp_and_print_results(n, c, r_cmp, sorted_results):
    print('n=', n, 'F_n=', r_cmp)
    for (alg, r_n, avr_n, std_n) in sorted_results:
        lo_n, hi_n = get_confint(avr_n, std_n, n)
        is_exact = 'False'
        if r_n == r_cmp:
            is_exact = 'True '
        print("alg={} exact={} t_avr={:.6f} t_std={:.6f} t_lo={} t_hi={}".format(alg, is_exact, avr_n, std_n, lo_n, hi_n))
        if c and (is_exact == 'False'):
            diff = compare_abs(r_n, r_cmp, False)
            ratio = compare_rel(r_n, r_cmp, True, '.6e')
            print("alg={:2d} exact={} r_n-r_3={:d} r_n/r_3={:.6f}".format(alg, is_exact, diff, ratio))

def main():
    n = None # n of F_n
    alg_ids = None  # algo ids selected
    nrepeats = 1 # num repeats for time calc
    c = False # compare (cmp) errors of approximate results
    p = False # print all numbers from F_0 to F_n

    usage = " -h/--help"
    usage += " -n/--nth=int>=0"
    usage += " [-a/--alg=int in [1..12]]"
    usage += " [-c/--cmp]"
    usage += " [-r/--repeat=int>0]"
    usage += " [-p/--print]"

    # get the arguments
    try:
        opts, _ = getopt.getopt(sys.argv[1:],
                                'hn:a:r:cp',
                                ['help', 'nth=', 'alg=', 'cmp=', 'repeat=', 'print'])
    except getopt.GetoptError as err:
        at_exit(err)

    for o, a in opts:
        try:
            if o in ('-n', '--nth'):
                n = int(a)
            elif o in ('-a', '--alg'):
                alg_ids = [int(x) for x in a.split(',')]
            elif o in ('-c', '--cmp'):
                c = True
            elif o in ('-r', '--repeat'):
                nrepeats = int(a)
                if nrepeats <= 0:
                    raise Exception()
            elif o in ('-p', '--print'):
                p = True
            else:
                raise Exception()
        except Exception as err:
            at_exit(err, 'Error', usage)

    if n is None:
        at_exit('', 'Error', usage)
    if alg_ids is None:
        alg_ids = [3]

    if p:
        # generate all the fib numbers from the 1st to the nth
        gen_all_fib_nums_upto(n)
    else:
        # run the other requested algos with the given ids
        sorted_results = run_requested_algos(n, alg_ids, nrepeats)

        # run ad_fib3 as the baseline
        r_cmp, _, _ = run(ad_fib3, n, nrepeats)

        # compare and print the results in the increasing runtime order
        cmp_and_print_results(n, c, r_cmp, sorted_results)

if __name__ == '__main__':
    main()

# EOF

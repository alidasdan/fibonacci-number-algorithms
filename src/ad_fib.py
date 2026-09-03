#!/usr/bin/env python3

# compute fibonacci numbers using multiple algorithms. this is a good
# exercise in alg development, including recursion vs iteration,
# dynamic programming w/ or w/o memoization, closed formula vs
# iteration, floating point errors.

# author: ali dasdan

import sys
import getopt
from math import sqrt
import importlib
from statistics import mean, stdev
from time import perf_counter
from typing import Any, List, Tuple
from types import ModuleType

from ad_util import alg_ids, negafib, at_exit, show_usage
import ad_fib3

# the id of the algorithm used as the correctness baseline. it is the
# simple linear-time iteration, i.e., the same algorithm as the
# fib_test oracle in ad_util.
BASELINE_ALG = 3

# generate all fib numbers from 0th to the nth using the iterative
# linear-time algorithm.
def fib_all(n:int) -> List[int]:
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

# get the confidence interval of the average runtime measured over
# nrepeats repetitions: avr +/- 1.96 * std / sqrt(nrepeats). note that
# the sample count here is the repetition count, not n.
def get_confint(avr:float, std:float, nrepeats:int, is_pos:bool=True, fmt_str:str='.6f') -> Tuple[str, str]:
    k = 0.0
    if nrepeats > 0:
        k = 1.96 * std / sqrt(nrepeats)
    lo = avr - k
    if is_pos:
        lo = max(0.0, lo)
    hi = avr + k
    return format(lo, fmt_str), format(hi, fmt_str)

# compare results in absolute. the caller formats the result.
def compare_abs(a:int, b:int) -> int:
    return a - b

# compare results in relative. the caller formats the result.
def compare_rel(a:int, b:int) -> float:
    if b == 0:
        return float(a)
    return float(abs(compare_abs(a, b))) / b

# run mod.fib(n) nrepeats times, also measure its runtime in seconds.
# if mod.fib raises, return the exception in place of the result so
# that one failing algorithm does not end the whole run.
def run(mod:ModuleType, n:int, nrepeats:int) -> Tuple[Any, float, float]:
    if nrepeats <= 0:
        nrepeats = 1
    r = None
    times = []
    for _ in range(nrepeats):
        t_start = perf_counter()
        try:
            r = mod.fib(n)
        except Exception as err:
            return err, 0.0, 0.0
        times.append(perf_counter() - t_start)
    avr = mean(times)
    std = stdev(times) if len(times) > 1 else 0.0
    return r, avr, std

### section: main

# generate all the fib numbers from the 1st to the nth
def gen_all_fib_nums_upto(n:int) -> None:
    start_all = perf_counter()
    try:
        h = fib_all(n)
    except Exception as err:
        at_exit(err)
    elapsed_all = perf_counter() - start_all
    print(h)
    print('time elapsed in s', elapsed_all)

# run the other requested algos with the given ids. the ids are used
# to construct the algo name, which in turn is used to construct the
# module name in runtime.
def run_requested_algos(n:int, ids:List[int], nrepeats:int) -> List[Tuple[Any, ...]]:
    results = []
    for alg_id in ids:
        alg_nm = 'ad_fib' + str(alg_id)
        try:
            mod = importlib.import_module(alg_nm, package=None)
        except ImportError:
            at_exit('no algorithm with the id ' + str(alg_id))
        r_n, avr_n, std_n = run(mod, n, nrepeats)
        results.append((alg_id, r_n, avr_n, std_n))

    # order by the average runtime, with the failed algos last.
    return sorted(results, key=lambda x: (isinstance(x[1], Exception), x[2]))

# compare and print the results in the increasing runtime order
def cmp_and_print_results(n:int, c:bool, r_cmp:int, nrepeats:int,
                          sorted_results:List[Tuple[Any, ...]]) -> None:
    print('n=', n, 'F_n=', r_cmp)
    for (alg, r_n, avr_n, std_n) in sorted_results:
        # an algorithm that raised, e.g. one that overflowed the
        # floating-point range, is reported without ending the run.
        if isinstance(r_n, Exception):
            print("alg= {} exact= {:5} error= '{}'".format(alg, 'ERROR', r_n))
            continue
        lo_n, hi_n = get_confint(avr_n, std_n, nrepeats)
        is_exact = (r_n == r_cmp)
        print("alg= {} exact= {!s:5} t_avr= {:.6f} t_std= {:.6f} t_lo= {} t_hi= {}".format(
            alg, is_exact, avr_n, std_n, lo_n, hi_n))
        if c and not is_exact:
            diff = compare_abs(r_n, r_cmp)
            ratio = compare_rel(r_n, r_cmp)
            print("alg= {} exact= {!s:5} r_n-r_{}= {:d} r_n/r_{}= {:.6e}".format(
                alg, is_exact, BASELINE_ALG, diff, BASELINE_ALG, ratio))

def main():
    n = None # n of F_n
    ids = None  # algo ids selected
    nrepeats = 1 # num repeats for time calc
    c = False # compare (cmp) errors of approximate results
    p = False # print all numbers from F_0 to F_n

    # the id range is read from the ad_fibN.py file names so that the
    # usage text cannot go stale as algorithms are added.
    all_ids = alg_ids()

    usage = " -h/--help"
    usage += " -n/--nth=int"
    usage += " [-a/--alg=comma-separated ids in [{}..{}]]".format(all_ids[0], all_ids[-1])
    usage += " [-c/--cmp]"
    usage += " [-r/--repeat=int>0]"
    usage += " [-p/--print]"

    # get the arguments
    try:
        opts, _ = getopt.getopt(sys.argv[1:],
                                'hn:a:r:cp',
                                ['help', 'nth=', 'alg=', 'cmp', 'repeat=', 'print'])
    except getopt.GetoptError as err:
        at_exit(err, 'Error', usage)

    for o, a in opts:
        try:
            if o in ('-h', '--help'):
                show_usage(usage)
                sys.exit(0)
            elif o in ('-n', '--nth'):
                n = int(a)
            elif o in ('-a', '--alg'):
                ids = [int(x) for x in a.split(',')]
            elif o in ('-c', '--cmp'):
                c = True
            elif o in ('-r', '--repeat'):
                nrepeats = int(a)
                if nrepeats <= 0:
                    raise Exception('the repeat count must be > 0')
            elif o in ('-p', '--print'):
                p = True
            else:
                raise Exception('unknown option ' + o)
        except Exception as err:
            at_exit(err, 'Error', usage)

    if n is None:
        at_exit('the -n/--nth option is required', 'Error', usage)
    if ids is None:
        ids = [BASELINE_ALG]

    if p:
        # generate all the fib numbers from the 1st to the nth
        gen_all_fib_nums_upto(n)
    else:
        # run the other requested algos with the given ids
        sorted_results = run_requested_algos(n, ids, nrepeats)

        # run ad_fib3 as the baseline, reusing the result already
        # measured above if the baseline was among the requested algos.
        r_cmp = None
        for (alg, r_n, _, _) in sorted_results:
            if alg == BASELINE_ALG:
                r_cmp = r_n
                break
        if r_cmp is None:
            r_cmp, _, _ = run(ad_fib3, n, nrepeats)
        if isinstance(r_cmp, Exception):
            at_exit(r_cmp, 'Error in the baseline alg ' + str(BASELINE_ALG))

        # compare and print the results in the increasing runtime order
        cmp_and_print_results(n, c, r_cmp, nrepeats, sorted_results)

if __name__ == '__main__':
    main()

# EOF

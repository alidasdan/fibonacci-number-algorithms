#!/usr/bin/python

# compute fibonacci numbers using multiple algorithms. this is a good
# exercise in alg development, including recursion vs iteration,
# dynamic programming w/ or w/o memoization, closed formula vs
# iteration, floating point errors.

# author: ali dasdan

import sys
import getopt
import math
from time import clock

from ad_util import *
import ad_fib1
import ad_fib2
import ad_fib3
import ad_fib4
import ad_fib5
import ad_fib6
import ad_fib7
import ad_fib8
import ad_fib9
import ad_fib10
import ad_fib11
import ad_fib12

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
def get_confint(avr, std, n, is_pos = True, do_fmt = True, fmt_str = '.6f'):
    k = 0.0
    if n > 0:
        try:
            k = 1.96 * math.sqrt(n)
        except Exception, msg:
            at_exit(msg)
    lo = avr - k * std
    if is_pos:
        lo = max(0.0, lo)
    hi = avr + k * std
    return format(lo, fmt_str), format(hi, fmt_str)
    
# compare results in absolute
def compare_abs(a, b, do_fmt = True, fmt_str = '.6f'):
    if do_fmt:            
        return format(a - b, fmt_str)
    else:
        return a - b

# compare results in relative
def compare_rel(a, b, do_fmt = True, fmt_str = '.6f'):
    diff = compare_abs(a, b, False)
    if b == 0:
        if do_fmt:
            return format(a, fmt_str)
        else:
            return a
    if do_fmt:
        return format(float(abs(diff)) / b, fmt_str)
    else:
        return float(abs(diff)) / b
        
# run mod.fib(n) nrepeats times, also measure its runtime in seconds.
def run(mod, n, nrepeats):
    sum = 0.0
    sum2 = 0.0
    for i in range(nrepeats):
        start = clock()
        try:
            r = mod.fib(n)
        except Exception, msg:
            at_exit(msg)
        t = clock() - start
        sum += t
        sum2 += t * t
    avr = float(sum) / nrepeats
    try:
        std = math.sqrt(sum2 / nrepeats - avr * avr)
    except Exception, msg:
        at_exit(msg)
    return r, avr, std

### section: main

def main():
    n = None # n of F_n
    algs = []  # algos selected
    nrepeats = 1 # num repeats for time calc
    c = False # compare (cmp) errors of approximate results
    p = False # print all numbers from F_0 to F_n

    usage = " -h/--help -n/--nth=int>=0 [-a/--alg=int in [1..12]] [-c/--cmp] [-r/--repeat=int>0] [-p/--print]"

    # get the arguments
    try:
        opts, args = getopt.getopt(sys.argv[1:],
                                   'hn:a:r:cp',
                                   ['help', 'nth=', 'alg=', 'cmp=', 'repeat=', 'print'])
    except getopt.GetoptError, msg:
        at_exit('')

    for o, a in opts:
        msg = ""
        try:
            if o in ('-h', '--help'):
                raise Exception()
            elif o in ('-n', '--nth'):
                n = int(a)
            elif o in ('-a', '--alg'):
                algs = [int(x) for x in a.split(',')]
            elif o in ('-c', '--cmp'):
                c = True
            elif o in ('-r', '--repeat'):
                nrepeats = int(a)
                if nrepeats <= 0: raise Exception()
            elif o in ('-p', '--print'):
                p = True
            else:
                raise Exception()
        except Exception, msg:
            at_exit(msg, 'Error', usage)

    if n == None:
        at_exit('', 'Error', usage)
    if algs == []:
        algs = [3]

    if p:
        # generate all the fib numbers from the 1st to the nth
        start_all = clock()
        h = fib_all(n)
        elapsed_all = clock() - start_all
        print h
        print 'time elapsed', elapsed_all
    else:
        # run ad_fib3 as the baseline
        r_cmp, avr_cmp, std_cmp = run(ad_fib3, n, nrepeats)

        # run the other requested algos
        results = []
        r_n = None
        for alg in algs:
            mod = 'ad_fib' + str(alg)
            if mod not in globals(): continue
            r_n, avr_n, std_n = run(globals()[mod], n, nrepeats)
            results.append((alg, r_n, avr_n, std_n))

        sorted_results = sorted(results, key=lambda x: x[2])

        fmt_str = '.6f'

        # compare and print the results in the increasing runtime order
        lo_cmp, hi_cmp = get_confint(avr_cmp, std_cmp, n)
        print 'n=', n, 'F_n=', r_cmp
        for (alg, r_n, avr_n, std_n) in sorted_results:
            lo_n, hi_n = get_confint(avr_n, std_n, n)
            is_exact = 'False'
            if r_n == r_cmp: is_exact = 'True '
            print 'alg=', format(alg, '2d'), 'exact=', is_exact, 't_avr=', format(avr_n, fmt_str), 't_std=', format(std_n, fmt_str), 't_lo=', lo_n, 't_hi=', hi_n
            if c and (is_exact == 'False'):
                diff = compare_abs(r_n, r_cmp, False)
                ratio = compare_rel(r_n, r_cmp, True, '.6e')
                print 'alg=', format(alg, '2d'), 'exact=', is_exact, 'r_n-r_3=', diff, 'r_n/r_3=', ratio

if __name__ == '__main__':
    main()

# EOF

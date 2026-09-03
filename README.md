# fibonacci-number-algorithms
==============================

This package contains multiple algorithms to compute the Fibonacci
numbers. The goal for this package is to help students learn the
basics of algorithms using simple algorithms so that they can focus
more on the algorithmic concepts illustrated.

The algorithms in this package illustrate the following rich set of
algorithmic concepts: Top-down vs. bottom-up dynamic programming,
dynamic programming with vs. without memoization, recursion
vs. iteration, integer vs. floating-point arithmetic, exact vs
approximate results, exponential- vs. polynomial-time, constant-time
vs non-constant-time arithmetic, constant to polynomial to exponential
time and space complexity, closed-form vs. recursive formulas,
repeated squaring vs. linear iteration for exponentiation, recursion
depth, and probably more.

The document 'fib_algos.pdf' in the 'doc/' directory lists a set of
homework questions for further study.

## FIBONACCI NUMBERS

The Fibonacci numbers are a sequence 'F(n)' (or 'F_n') of integers in
which every number after the first two, 0 and 1, is the sum of the two
preceding numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, ... More formally,
they are defined by the recurrence relation 'F_n = F(n-1) + F(n-2)',
'n >= 2', with the base values 'F(0)=0' and 'F(1)=1'.

## ALGORITHMS FOR FIBONACCI NUMBERS

The recurrence relation given above directly maps to arguably the
simplest algorithm to compute the Fibonacci numbers. There are many
other formulas to derive the Fibonacci numbers and many of them also
map to simple algorithms. This package contains 15+ such algorithms
(when this repository was first created, the number was 12). Each 
algorithm takes in an integer 'n' and returns the corresponding 
Fibonacci number 'F(n)' (or 'F_n').

For simplicity, each algorithm is named as 'fibN' where 'N' ranges
from 1 to 15. Each algorithm 'fibN' is implemented in a separate
program file 'ad_fibN.py'. These files are included as modules in
'ad_fib.py' program for experimental comparisons. The algorithm ids
are read from the 'ad_fibN.py' file names at runtime, so adding an
algorithm needs no change anywhere else.

The document 'fib_algos.pdf' in the 'doc/' directory provides far more
information about these algorithms.

## HOW TO RUN

This package contains programs written in the Python programming
language (Python 3.7.3+). Each 'ad_fibN.py' can be run by simply
typing its name without any arguments. Each 'ad_fibN.py' tests its
algorithm against a test algorithm from 'ad_util.py' and prints
'success' if the test succeeds. If the test fails, there will be an
assertion failure message.

These algorithms in 'ad_fibN.py' are included as modules in the main
program 'ad_fib.py'. Its usage is shown below.

```
ad_fib.py
   -h/--help
   -n/--nth=int               # n for F(n); a negative n gives F(-n)
   [-a/--alg=ids in [1..15]]  # one algo id, or several separated by commas
   [-c/--cmp]                 # compare results if not exact
   [-r/--repeat=int>0]        # num repetitions for averaging and ranking
   [-p/--print]               # print all F(n) from F(0) to F(n)
```

Here is an example run with all the algorithms from 'fib1' to 'fib15'
and its output.

```
> ad_fib.py -n 10 -a 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15 -r 1
n= 10 F_n= 55
alg= 3 exact= True  t_avr= 0.000003 t_std= 0.000000 t_lo= 0.000003 t_hi= 0.000003
alg= 13 exact= True  t_avr= 0.000004 t_std= 0.000000 t_lo= 0.000004 t_hi= 0.000004
alg= 5 exact= True  t_avr= 0.000005 t_std= 0.000000 t_lo= 0.000005 t_hi= 0.000005
alg= 15 exact= True  t_avr= 0.000005 t_std= 0.000000 t_lo= 0.000005 t_hi= 0.000005
alg= 14 exact= True  t_avr= 0.000005 t_std= 0.000000 t_lo= 0.000005 t_hi= 0.000005
alg= 2 exact= True  t_avr= 0.000007 t_std= 0.000000 t_lo= 0.000007 t_hi= 0.000007
alg= 12 exact= True  t_avr= 0.000008 t_std= 0.000000 t_lo= 0.000008 t_hi= 0.000008
alg= 4 exact= True  t_avr= 0.000008 t_std= 0.000000 t_lo= 0.000008 t_hi= 0.000008
alg= 9 exact= True  t_avr= 0.000009 t_std= 0.000000 t_lo= 0.000009 t_hi= 0.000009
alg= 6 exact= True  t_avr= 0.000010 t_std= 0.000000 t_lo= 0.000010 t_hi= 0.000010
alg= 8 exact= True  t_avr= 0.000011 t_std= 0.000000 t_lo= 0.000011 t_hi= 0.000011
alg= 7 exact= True  t_avr= 0.000013 t_std= 0.000000 t_lo= 0.000013 t_hi= 0.000013
alg= 10 exact= True  t_avr= 0.000019 t_std= 0.000000 t_lo= 0.000019 t_hi= 0.000019
alg= 11 exact= True  t_avr= 0.000019 t_std= 0.000000 t_lo= 0.000019 t_hi= 0.000019
alg= 1 exact= True  t_avr= 0.000021 t_std= 0.000000 t_lo= 0.000021 t_hi= 0.000021

```

The first line shows 'n' and 'F(n)' (as 'F_n'). Next comes one line
per algorithm, in the increasing order of the runtimes 't_avg'.

In the line for an algorithm 'fibN', 'alg' is N, 'exact' shows whether
or not the returned result of 'fibN' is exactly equal to 'F(n)',
't_avg' is the average runtime over 'R' repetitions (the argument to
the '-r' option), 't_std' is the standard deviation of the runtimes
over all the repetitions, and 't_lo' and 't_hi' are the low and high
bounds of the 95% confidence interval around the average runtime,
i.e., 't_avg' plus and minus '1.96 * t_std / sqrt(R)'.

An algorithm that raises, such as 'fib4' and 'fib5' above n=1474 where
the floating-point range overflows, is reported as 'exact= ERROR' with
its message, and the remaining algorithms still run.

## HOW TO TEST

Type 'utest.sh'. It prints 'success' or 'failure' for each check, one
per line, then a summary, and it exits with a nonzero status if any
check failed.

It runs three kinds of checks:
- 'ad_util.py' checks the 'fib_test' oracle that everything else is
compared against, by asserting it against published Fibonacci values.
This runs first, since no other check means anything if it fails;
- each 'ad_fibN.py' checks its own algorithm against that oracle for
the first 10 Fibonacci numbers;
- 'ad_test.py' checks every algorithm against the oracle over a much
wider range of 'n' and over negative 'n'. The algorithms that use
floating-point arithmetic are exact only up to a limit -- 'fib4' and
'fib5' up to n=70, 'fib12' up to n=78 -- and 'ad_test.py' asserts
those limits exactly, so a limit that moves in either direction is
reported as a failure.

## DOC/ DIRECTORY

The 'doc/' directory contains the following resources:
- 'fib_algos.pdf' is the paper with all the information about this
study, built from 'arxiv/fib.tex';
- 'results.how.algos.sh' is the bash file to run the algorithms for
the experimental study reported in the 'fib_algos.pdf' paper;
- 'results.how.plots.sh' is the bash file to generate the plots for
the experimental study reported in the 'fib_algos.pdf' paper;
- 'png/' is the plots from the experimental study reported in the 'fib_algos.pdf' paper;
- 'gp/' is the directory that contains the 'gnuplot' command files to
generate the plots under 'png/'.

Running 'results.how.algos.sh' creates a 'results/' directory with the
measurements it collects. That directory is not checked in.

Also see the document 'fib_algos.pdf' for the references to the source
of each algorithm.

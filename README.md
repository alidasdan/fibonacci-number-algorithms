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
map to simple algorithms. This package contains twelve such algorithms
(when this repository was first created). Each algorithm takes in an
integer 'n' and returns the corresponding Fibonacci number 'F(n)' (or
'F_n').

For simplicity, each algorithm is named as 'fibN' where 'N' ranges
from 1 to 12. Each algorithm 'fibN' is implemented in a separate
program file 'ad_fibN.py'. These files are included as modules in
'ad_fib.py' program for experimental comparisons.

The document 'fib_algos.pdf' in the 'doc/' directory provides far more
information about these algorithms.

## HOW TO RUN

This package contains programs written in the Python programming
language. Each 'ad_fibN.py' can be run by simply typing its name
without any arguments. Each 'ad_fibN.py' tests its algorithm against a
test algorithm from 'ad_util.py' and prints 'success' if the test
succeeds. If the test fails, there will be an assertion failure
message.

These algorithms in 'ad_fibN.py' are included as modules in the main
program 'ad_fib.py'. Its usage is shown below.

```
" -h/--help -n/--nth=int>=0 [-a/--alg=int in [1..12]] [-c/--cmp]
[-r/--repeat=int>0] [-p/--print]"
ad_fib.py
   -h/--help
   -n/--nth=int>=0            # n for F(n)
   [-a/--alg=int in [1..12]]  # the algo id, from 1 to 12
   [-c/--cmp]                 # compare results if not exact
   [-r/--repeat=int>0]        # num repetitions for averaging and ranking
   [-p/--print]               # print all F(n) from F(0) to F(n)
```

Here is an example run with all the algorithms from 'fib1' to 'fib12'
and its output. 

```
> ad_fib.py -n 10 -a 1,2,3,4,5,6,7,8,9,10,11,12 -r 1
n= 10 F_n= 55
alg=  3 exact= True  t_avr= 0.000002 t_std= 0.000000 t_lo= 0.000002 t_hi= 0.000002
alg=  5 exact= True  t_avr= 0.000004 t_std= 0.000000 t_lo= 0.000004 t_hi= 0.000004
alg= 12 exact= True  t_avr= 0.000005 t_std= 0.000000 t_lo= 0.000005 t_hi= 0.000005
alg=  9 exact= True  t_avr= 0.000006 t_std= 0.000000 t_lo= 0.000006 t_hi= 0.000006
alg=  2 exact= True  t_avr= 0.000010 t_std= 0.000000 t_lo= 0.000010 t_hi= 0.000010
alg=  7 exact= True  t_avr= 0.000013 t_std= 0.000000 t_lo= 0.000013 t_hi= 0.000013
alg=  8 exact= True  t_avr= 0.000013 t_std= 0.000000 t_lo= 0.000013 t_hi= 0.000013
alg= 11 exact= True  t_avr= 0.000014 t_std= 0.000000 t_lo= 0.000014 t_hi= 0.000014
alg=  6 exact= True  t_avr= 0.000015 t_std= 0.000000 t_lo= 0.000015 t_hi= 0.000015
alg= 10 exact= True  t_avr= 0.000015 t_std= 0.000000 t_lo= 0.000015 t_hi= 0.000015
alg=  1 exact= True  t_avr= 0.000030 t_std= 0.000000 t_lo= 0.000030 t_hi= 0.000030
alg=  4 exact= True  t_avr= 0.000047 t_std= 0.000000 t_lo= 0.000047 t_hi= 0.000047

```

The first line shows 'n' and 'F(n)' (as 'F_n'). Next comes one line
per algorithm, in the increasing order of the runtimes 't_avg'.

In the line for an algorithm 'fibN', 'alg' is N, 'exact' shows whether
or not the returned result of 'fibN' is exactly equal to 'F(n)',
't_avg' is the average runtime over 'R' repetitions (the argument to
the '-r' option), 't_std' is the standard deviation of the runtimes
over all the repetitions, and 't_lo' and 't_hi' are the low and high
bounds of the confidence interval around the average runtime.

## HOW TO TEST

Type 'utest.sh'. Since each algorithm 'fibN' implemented in
'ad_fibN.py' tests itself. It should 'success' for each algorithm.

## DOC/ DIRECTORY

The 'doc/' directory contains the following resources:
- 'fib_algos.pdf' is the paper with all the information about this
study;
- 'resources.how.algos.sh' is the bash file to run the algorithms for
the experimental study reported in the 'fib_algos.pdf' paper;
- 'resources.how.plots.sh' is the bash file to generate the plots for
the experimental study reported in the 'fib_algos.pdf' paper;
- 'png1/' is the directory that contains the images of each algorithm,
as implemented in the Python programming language;
- 'png2/' is the plots from the experimental study reported in the 'fib_algos.pdf' paper;
- 'gp/' is the directory that contains the 'gnuplot' command files to
generate the plots under 'png2/';
- 'results/' is the directory that contains the results when
'resources.how.algos.sh' is run.

Also see the document 'fib_algos.pdf' for the references to the source
of each algorithm.

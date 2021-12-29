#!/bin/bash

# run as 'source this_file'
# at the parent dir of results

if [ -d result.save ]; then echo 'rename results.save'; exit; fi

# create result directory and files
if [ -d results ]; then \mv results results.save; fi
mkdir results

# set the path to algos
apath=../src

# get the number of fib algorithms
cnt=`ls -l $apath/ad_fib?*.py|wc -l`

# results without fib1
for ((a=2; a<=$cnt; a+=1)); do
    \rm results/fib$a.30; touch results/fib$a.30;
    for ((i=0; i<=30; i+=1)); do
        echo '1' $a $i;
        $apath/ad_fib.py -n $i -a $a -r 10000 >> results/fib$a.30;
    done;
done

# results without fib1, up to 70 where all results are exact
for ((a=2; a<=$cnt; a+=1)); do
    \rm results/fib$a.70; touch results/fib$a.70;
    for ((i=0; i<=70; i+=1)); do
        echo '2' $a $i;
        $apath/ad_fib.py -n $i -a $a -r 10000 >> results/fib$a.70;
    done;
done

# results without fib1, up to the limits of recursion
for ((a=2; a<=$cnt; a+=1)); do
    \rm results/fib$a.900; touch results/fib$a.900;
    for ((i=0; i<=900; i+=10)); do
        echo '3' $a $i;
        $apath/ad_fib.py -n $i -a $a -r 10000 >> results/fib$a.900;
    done;
done

# results with iterative & exact algos, no recursion
for a in 3 6 8 10 11 12 14; do
    \rm results/fib$a.10k; touch results/fib$a.10k;
    for ((i=0; i<=10000; i+=100)); do
        echo '4' $a $i;
        $apath/ad_fib.py -n $i -a $a -r 10000 >> results/fib$a.10k;
    done;
done

# results with fib1 only
for ((a=1; a<=1; a+=1)); do
    \rm results/fib$a.30; touch results/fib$a.30;
    for ((i=0; i<=30; i+=1)); do
        echo '5' $a $i;
        $apath/ad_fib.py -n $i -a $a -r 10000 >> results/fib$a.30;
    done;
done

# EOF

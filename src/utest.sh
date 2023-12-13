#!/bin/bash

# get the number of fib algorithms
cnt=`ls -l ad_fib?*.py|wc -l`

# test each algorithm; runs for the 1st 10 fib numbers
for ((i=1;i<=$cnt;++i)); do
    echo -n "test ad_fib$i.py "
    ./ad_fib$i.py
done

# check for the correct algo call
for ((i=1;i<=$cnt;i=i+2)); do
    echo -n "find ad_fib$i in ad_fib.py output "
    c=$(./ad_fib.py -n 10 -a $i | grep -c "alg= "$i" ")
    if [[ $c -eq 1 ]]; then
        echo 'success'
    fi
    if [[ $c -eq 0 ]]; then
        echo 'failure'
    fi
done

# check for the correct algo call
for ((i=2;i<=$cnt;i=i+2)); do
    echo -n "do not find ad_fib$i in ad_fib.py output "
    c=$(./ad_fib.py -n 10 -a $(($i-1)) | grep -c "alg= "$i" ")
    if [[ $c -eq 1 ]]; then
        echo 'failure'
    fi
    if [[ $c -eq 0 ]]; then
        echo 'success'
    fi
done


# EOF

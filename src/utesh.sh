#!/bin/bash

for i in {1..12}; do
    echo -n "test ad_fib$i.py "
    ./ad_fib$i.py
done

for i in {1..6}; do
    echo -n "find ad_fib$i in ad_fib.py output "
    c=$(./ad_fib.py -n 10 -a 1,2,3,4,5,6 | grep -c "alg="$i" ")
    if [[ $c -eq 1 ]]; then
        echo 'success'
    fi
    if [[ $c -eq 0 ]]; then
        echo 'failure'
    fi
done

for i in {1..6}; do
    echo -n "do not find ad_fib$i in ad_fib.py output "
    c=$(./ad_fib.py -n 10 -a 7,8,9,10,11,12 | grep -c "alg="$i" ")
    if [[ $c -eq 1 ]]; then
        echo 'failure'
    fi
    if [[ $c -eq 0 ]]; then
        echo 'success'
    fi
done


# EOF

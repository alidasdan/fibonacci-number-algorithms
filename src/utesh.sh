#!/bin/bash

cnt=`ls -l ad_fib?*.py|wc -l`

for ((i=1;i<=$cnt;++i)); do
    echo -n "test ad_fib$i.py "
    ./ad_fib$i.py
done

for ((i=1;i<=$cnt;++i)); do
    if [[ $(($i % 2)) -eq 0 ]]; then
        continue
    fi
    echo -n "find ad_fib$i in ad_fib.py output "
    c=$(./ad_fib.py -n 10 -a $i | grep -c "alg="$i" ")
    if [[ $c -eq 1 ]]; then
        echo 'success'
    fi
    if [[ $c -eq 0 ]]; then
        echo 'failure'
    fi
done

for ((i=1;i<=$cnt;++i)); do
    if [[ $(($i % 2)) -eq 1 ]]; then
        continue
    fi
    echo -n "do not find ad_fib$i in ad_fib.py output "
    c=$(./ad_fib.py -n 10 -a $(($i+1)) | grep -c "alg="$i" ")
    if [[ $c -eq 1 ]]; then
        echo 'failure'
    fi
    if [[ $c -eq 0 ]]; then
        echo 'success'
    fi
done


# EOF

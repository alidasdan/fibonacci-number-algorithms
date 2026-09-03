#!/bin/bash

# unit tests for the fibonacci algorithms. every check prints
# 'success' or 'failure', and the script exits nonzero if any check
# fails, so that a caller or a CI job can detect a regression.

nfail=0
ntest=0

# report one check: $1 is the description, $2 is 'success' or 'failure'
check() {
    ntest=$((ntest + 1))
    echo "$1 $2"
    if [[ "$2" != 'success' ]]; then
        nfail=$((nfail + 1))
    fi
}

# run a program and report whether it succeeded, i.e., whether it
# exited 0 and printed 'success'
run_prog() {
    local desc="$1"
    shift
    local out rc
    out=$("$@" 2>&1)
    rc=$?
    if [[ $rc -eq 0 && "$out" == 'success' ]]; then
        check "$desc" 'success'
    else
        check "$desc" "failure (rc=$rc out='$out')"
    fi
}

# get the algorithm ids from the file names rather than assuming that
# they run contiguously from 1
ids=$(ls ad_fib?*.py | sed -e 's/^ad_fib//' -e 's/\.py$//' | sort -n)

# test the oracle first: every algorithm below is checked against it,
# so nothing else means anything if this fails
run_prog "test ad_util.py" ./ad_util.py

# test each algorithm against the oracle; runs for the 1st 10 fib numbers
for i in $ids; do
    run_prog "test ad_fib$i.py" "./ad_fib$i.py"
done

# test every algorithm over a wide range of n and over negative n
run_prog "test ad_test.py" ./ad_test.py

# check that ad_fib.py runs exactly the algorithm it was asked for:
# the requested id must appear in the output and the previous id in
# the list must not
prev=''
for i in $ids; do
    out=$(./ad_fib.py -n 10 -a "$i" 2>&1)

    c=$(echo "$out" | grep -c "alg= $i ")
    if [[ $c -eq 1 ]]; then
        check "find ad_fib$i in ad_fib.py output" 'success'
    else
        check "find ad_fib$i in ad_fib.py output" 'failure'
    fi

    if [[ -n "$prev" ]]; then
        c=$(echo "$out" | grep -c "alg= $prev ")
        if [[ $c -eq 0 ]]; then
            check "do not find ad_fib$prev in ad_fib.py output" 'success'
        else
            check "do not find ad_fib$prev in ad_fib.py output" 'failure'
        fi
    fi

    prev=$i
done

echo
if [[ $nfail -eq 0 ]]; then
    echo "all $ntest tests passed"
    exit 0
fi
echo "$nfail of $ntest tests FAILED"
exit 1

# EOF

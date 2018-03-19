#!/bin/bash

# run as 'source this_file'
# at the parent dir of results

cd results

# generate the timings

for i in fib*.30 fib*.70 fib*.900 fib*.10k; do
    echo $i;
    grep 'n=' $i | awk '{print $2}' > $i.1;
done
for i in fib*.30 fib*.70 fib*.900 fib*.10k; do
    echo $i;
    grep 'alg=' $i | awk '{print $6,$8}' > $i.2;
done
for i in fib*.30 fib*.70 fib*.900 fib*.10k; do
    echo $i;
    paste $i.1 $i.2 > $i.time;
done
for i in fib*.30 fib*.70 fib*.900 fib*.10k; do
    echo $i;
    \rm $i.1 $i.2;
done

# generate plots

for i in ../gp/*.gp; do
    echo $i;
    gnuplot < $i;
done
for i in *.png; do
    echo $i;
    \mv $i ../png2;
done

# generate ranks

for i in 30 70 900 10k; do
    echo $i
    \rm rank.$i
    for j in *$i.time; do awk '{s+=$2}END{printf("%s %.6f\n", ARGV[1], s)}' $j; done | sort -n -k 2,2 >> rank.$i
done

cd ..

# EOF

set terminal png enhanced
set output 'fib_30_cv.png'
set grid
set key reverse Left outside
set xrange [0:30]
set xtics 5
set xlabel 'n of the nth Fibonacci number F_n'
set ylabel 'Coefficient of variation'
set format y '%.2e'
plot \
'fib1.30.time' using 1:($2>0?$3/$2:$2) t 'fib1(n)' w linesp lw 2 ps 2, \
'fib2.30.time' using 1:($2>0?$3/$2:$2) t 'fib2(n)' w linesp lw 2 ps 2, \
'fib3.30.time' using 1:($2>0?$3/$2:$2) t 'fib3(n)' w linesp lw 2 ps 2, \
'fib4.30.time' using 1:($2>0?$3/$2:$2) t 'fib4(n)' w linesp lw 2 ps 2, \
'fib5.30.time' using 1:($2>0?$3/$2:$2) t 'fib5(n)' w linesp lw 2 ps 2, \
'fib6.30.time' using 1:($2>0?$3/$2:$2) t 'fib6(n)' w linesp lw 2 ps 2, \
'fib7.30.time' using 1:($2>0?$3/$2:$2) t 'fib7(n)' w linesp lw 2 ps 2, \
'fib8.30.time' using 1:($2>0?$3/$2:$2) t 'fib8(n)' w linesp lw 2 ps 2, \
'fib9.30.time' using 1:($2>0?$3/$2:$2) t 'fib9(n)' w linesp lw 2 ps 2, \
'fib10.30.time' using 1:($2>0?$3/$2:$2) t 'fib10(n)' w linesp lw 2 ps 2, \
'fib11.30.time' using 1:($2>0?$3/$2:$2) t 'fib11(n)' w linesp lw 2 ps 2, \
'fib12.30.time' using 1:($2>0?$3/$2:$2) t 'fib12(n)' w linesp lw 2 ps 2
quit


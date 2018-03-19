set terminal png
set output 'fib_70.png'
set grid
set key reverse Left outside
set xrange [0:70]
set xlabel 'n of the nth Fibonacci number F_n'
set ylabel 'Running time in seconds'
set format y '%.2e'
plot \
'fib2.70.time' using 1:2 t 'fib2(n)' w linesp lw 2 ps 2, \
'fib3.70.time' using 1:2 t 'fib3(n)' w linesp lw 2 ps 2, \
'fib4.70.time' using 1:2 t 'fib4(n)' w linesp lw 2 ps 2, \
'fib5.70.time' using 1:2 t 'fib5(n)' w linesp lw 2 ps 2, \
'fib6.70.time' using 1:2 t 'fib6(n)' w linesp lw 2 ps 2, \
'fib7.70.time' using 1:2 t 'fib7(n)' w linesp lw 2 ps 2, \
'fib8.70.time' using 1:2 t 'fib8(n)' w linesp lw 2 ps 2, \
'fib9.70.time' using 1:2 t 'fib9(n)' w linesp lw 2 ps 2, \
'fib10.70.time' using 1:2 t 'fib10(n)' w linesp lw 2 ps 2, \
'fib11.70.time' using 1:2 t 'fib11(n)' w linesp lw 2 ps 2
quit


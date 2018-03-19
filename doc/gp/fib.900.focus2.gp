set terminal png enhanced
set output 'fib_900_focus2.png'
set grid
set key reverse Left outside
set xrange [0:900]
set xtics 100
set xlabel 'n of the nth Fibonacci number F_n'
set ylabel 'Running time in seconds'
set format y '%.2e'
plot \
'fib7.900.time' using 1:2 t 'fib7(n)' w linesp lw 2 ps 2, \
'fib8.900.time' using 1:2 t 'fib8(n)' w linesp lw 2 ps 2, \
'fib9.900.time' using 1:2 t 'fib9(n)' w linesp lw 2 ps 2, \
'fib10.900.time' using 1:2 t 'fib10(n)' w linesp lw 2 ps 2
quit


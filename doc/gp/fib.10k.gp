set terminal png enhanced
set output 'fib_10k.png'
set grid
set key reverse Left outside
set xrange [0:10000]
set xtics 1000
set xtics rotate by -45
set xlabel 'n of the nth Fibonacci number F_n'
set ylabel 'Running time in seconds'
set format y '%.2e'
plot \
'fib3.10k.time' using 1:2 t 'fib3(n)' w linesp lw 2 ps 2, \
'fib6.10k.time' using 1:2 t 'fib6(n)' w linesp lw 2 ps 2, \
'fib8.10k.time' using 1:2 t 'fib8(n)' w linesp lw 2 ps 2, \
'fib10.10k.time' using 1:2 t 'fib10(n)' w linesp lw 2 ps 2, \
'fib11.10k.time' using 1:2 t 'fib11(n)' w linesp lw 2 ps 2
quit


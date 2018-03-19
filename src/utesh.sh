#!/bin/bash

for i in {1..11};
do
    echo -n "./ad_fib$i.py "
    ./ad_fib$i.py
done

# EOF

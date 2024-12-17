#!/bin/bash

START=1
END=25
for day in $(seq $START $END); do
    if [ "$day" -lt 10 ]; then
        day="0$day"
    fi
    mkdir "day$day"
    cd "day$day" || exit
    touch input.txt
    cat <<EOF > s.py 
with open('./day$day/input.txt', 'r') as f:
    ans1 = 0
    
    print(ans1)
    
    ans2 = 0
    
    print(ans2)
EOF
    cd ..
done
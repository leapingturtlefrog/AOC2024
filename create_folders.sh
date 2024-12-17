#!/bin/bash

START=7
END=25
for day_unpadded in $(seq $START $END); do
    day=$(printf "%02d" $day_unpadded)
    dir="day$day"
    if [ ! -d "$dir" ]; then
        mkdir "$dir"
    fi
    cd "day$day" || exit
    if [ ! -f "input.txt" ]; then
        touch input.txt
    fi
    if [ ! -f "s.py" ]; then
        cat <<EOF > s.py
with open('./day$day/input.txt', 'r') as f:
    ans1 = 0
    
    print(ans1)
    
    ans2 = 0
    
    print(ans2)
EOF
    fi
    cd ..
done
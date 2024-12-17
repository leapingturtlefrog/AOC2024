#!/bin/bash

# Usage: './benchmark.sh [number-of-days]'

cmd="hyperfine --warmup 2 --runs 10 --export-markdown benchmarks.md"
for day in $(seq 1 $1); do
    cmd+=" \"python ./day$day/s.py\""
done
eval $cmd

sed -i -e "s%\`python ./day%%g" -e "s%/s.py\`%%g" -e "s/|[^|]*|[^|]*\$//" ./benchmarks.md
sed -i "1c\| Day | Mean Execution Time (ms) | Min (ms) | Max (ms) | Peak Memory Usage (MB) |" ./benchmarks.md
sed -i "2c\|:---|---:|---:|---:|---:|" ./benchmarks.md

for l_num in $(seq 3 $(($1 + 2))); do
    memory_usage_kb=$(/usr/bin/time -f "%M" python ./day$(($l_num - 2))/s.py 2>&1 | tail -n 1)
    memory_usage_mb=$(echo "scale=2;" $memory_usage_kb / 1024 | bc)
    echo "Memory usage for day $(($l_num - 2)): ${memory_usage_mb} MB"
    sed -i "${l_num}s/$/| ${memory_usage_mb} |/" ./benchmarks.md
done

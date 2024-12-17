#!/bin/bash

# Usage: './benchmark.sh [number-of-days]'

cmd=("hyperfine" "--warmup" "2" "--runs" "10" "--export-markdown" "benchmarks.md")
for day_unpadded in $(seq 1 $1); do
    cmd+=("python ./day$(printf "%02d" $day_unpadded)/s.py")
done
"${cmd[@]}"

sed -i -e "s%\`python ./day%%g" -e "s%/s.py\`%%g" -e "s/|[^|]*|[^|]*\$//" ./benchmarks.md
sed -i -e "1c\| Day | Mean Execution Time (ms) | Min (ms) | Max (ms) | Peak Memory Usage (MB) |" \
        -e "2c\|:---|---:|---:|---:|---:|" ./benchmarks.md

for l_num in $(seq 3 $(($1 + 2))); do
    day=$(printf "%02d" $(($l_num - 2)))
    memory_usage_kb=$(/usr/bin/time -f "%M" python ./day${day}/s.py 2>&1 | tail -n 1)
    memory_usage_mb=$(echo "scale=2;" $memory_usage_kb / 1024 | bc)
    echo "Memory usage for day ${day}: ${memory_usage_mb} MB"
    sed -i "${l_num}s/$/| ${memory_usage_mb} |/" ./benchmarks.md
done

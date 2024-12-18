#!/bin/bash

# Usage: './update.sh'

if [ ! -f "./benchmarks.md" ]; then
    ./benchmark.sh 1
fi

next_day=$(( $(wc -l < ./benchmarks.md) - 1 ))

cmd=("hyperfine" "--warmup" "2" "--runs" "5" "--time-unit" "millisecond" "--export-markdown" "temp_benchmarks.md")
for day_unpadded in $(seq $next_day 25); do
    day=$(printf "%02d" $day_unpadded)
    if [ -s "./day$day/input.txt" ]; then
        cmd+=("python ./day$day/s.py")
    fi
done
if [ ${#cmd[@]} -gt 9 ]; then
    "${cmd[@]}"
    sed -i -e "s%\`python ./day%%g" -e "s%/s.py\`%%g" -e "s/|[^|]*|[^|]*\$//" ./temp_benchmarks.md

    for day_unpadded in $(seq $next_day 25); do
        day=$(printf "%02d" $day_unpadded)
        if [ -s "./day$day/input.txt" ]; then
            memory_usage_kb=$(/usr/bin/time -f "%M" python ./day${day}/s.py 2>&1 | tail -n 1)
            memory_usage_mb=$(echo "scale=2; $memory_usage_kb / 1024" | bc)
            echo "Memory usage for day ${day}: ${memory_usage_mb} MB"
            l_num=$(($day_unpadded - $next_day + 3))
            sed -i "${l_num}s/$/| ${memory_usage_mb} |/" ./temp_benchmarks.md
        fi
    done

    tail -n +3 temp_benchmarks.md >> ./benchmarks.md
    rm ./temp_benchmarks.md
else
    echo "No new scripts detected to be benchmarked."
fi

cat > "./README.md" <<EOF
## Advent of Code 2024
[adventofcode.com/2024](https://adventofcode.com/2024)

Solutions written in Python.

Benchmark results for the days that I have completed:
EOF
cat ./benchmarks.md >> ./README.md
echo -e "\n*Note: I made the benchmark to work with any programming language executed on Linux or WSL using hyperfine and the built-in GNU time command." >> ./README.md
echo "README.md updated."
import math

LINES = 1000

sum = 0

with open('input.txt', 'r') as f:
    for _ in range(LINES):
        twoNumsArr = f.readline().split('   ')
        sum += abs(int(twoNumsArr[0]) - int(twoNumsArr[1]))
    print(sum)
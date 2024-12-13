LINES = 1000

leftList = []
rightList = []
dif_sum = 0

with open('./day1/input.txt', 'r') as f:
    for line in f:
        numsPair = line.split('   ')
        leftList.append(int(numsPair[0]))
        rightList.append(int(numsPair[1]))

leftList.sort()
rightList.sort()
for i in range(LINES):
    dif_sum += abs(int(leftList[i]) - int(rightList[i]))
print(dif_sum)

min_idx = 0
sim_score = 0

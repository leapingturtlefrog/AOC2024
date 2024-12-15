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
print(dif_sum) # Part 1 answer

min_idx = 0
sim_score = 0
for num in leftList:
    for j in range(min_idx, LINES):
        if rightList[j] > num:
            break
        
        if rightList[j] == num:
            sim_score += num
        elif rightList[j] < num:
            min_idx += 1
print(sim_score) # Part 2 answer
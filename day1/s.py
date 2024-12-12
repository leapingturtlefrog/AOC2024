LINES = 1000

leftList = []
rightList = []

def bubble(lst):
    for i in range(len(lst) - 1, 0, -1):
        if (lst[i] < lst[i - 1]):
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
        else:
            break

def sum():
    dif = 0
    for i in range(LINES):
        dif += abs(int(leftList[0]) - int(rightList[1]))
    return dif

with open('input.txt', 'r') as f:
    for _ in range(LINES):
        numsPair = f.readline().split('   ')
        leftList.append(int(numsPair[0]))
        bubble(leftList)
        rightList.append(int(numsPair[1]))
        bubble(rightList)
print(sum())
DX_LIST = [-1, 0, 1, -1, 1, -1, 0, 1]
DY_LIST = [1, 1, 1, 0, 0, -1, -1, -1]

def present(lst, x, y, dx, dy):
    try:
        if y+3*dy > -1 and x+3*dx > -1 and \
                lst[y][x] == 'X' and lst[y+dy][x+dx] == 'M' and \
                lst[y+2*dy][x+2*dx] == 'A' and lst[y+3*dy][x+3*dx] == 'S':
            return 1
        else:
            return 0
    except IndexError:
        return 0

with open('./day04/input.txt', 'r') as f:
    ans = 0
    lst = f.read().split('\n')
    for j in range(len(lst)):
        for i in range(len(lst[0])):
            for pos in range(8):
                ans += present(lst, i, j, DX_LIST[pos], DY_LIST[pos])
    print(ans) # part 1
    
    ans2 = 0
    for j in range(1, len(lst) - 1):
        for i in range(1, len(lst[0]) - 1):
            if lst[j][i] == 'A' and \
                    (lst[j-1][i-1] == 'M' and lst[j+1][i+1] == 'S' or \
                     lst[j+1][i+1] == 'M' and lst[j-1][i-1] == 'S') and \
                    (lst[j-1][i+1] == 'M' and lst[j+1][i-1] == 'S' or \
                     lst[j+1][i-1] == 'M' and lst[j-1][i+1] == 'S'):
                ans2 += 1
    print(ans2) # part 2
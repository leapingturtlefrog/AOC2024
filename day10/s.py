def find_next(grid, x, y, seen, w, h):
    curr = grid[y][x]
    if curr == 9:
        seen[x+w*y] = True
        return
    if -1 < x - 1 < w and grid[y][x - 1] == curr + 1:
        find_next(grid, x - 1, y, seen, w, h)
    if -1 < x + 1 < w and grid[y][x + 1] == curr + 1:
        find_next(grid, x + 1, y, seen, w, h)
    if -1 < y - 1 < h and grid[y - 1][x] == curr + 1:
        find_next(grid, x, y - 1, seen, w, h)
    if -1 < y + 1 < h and grid[y + 1][x] == curr + 1:
        find_next(grid, x, y + 1, seen, w, h)
    return

def find_next2(grid, x, y, total, w, h):
    curr = grid[y][x]
    if curr == 9:
        total[0] += 1
        return
    if -1 < x - 1 < w and grid[y][x - 1] == curr + 1:
        find_next2(grid, x - 1, y, total, w, h)
    if -1 < x + 1 < w and grid[y][x + 1] == curr + 1:
        find_next2(grid, x + 1, y, total, w, h)
    if -1 < y - 1 < h and grid[y - 1][x] == curr + 1:
        find_next2(grid, x, y - 1, total, w, h)
    if -1 < y + 1 < h and grid[y + 1][x] == curr + 1:
        find_next2(grid, x, y + 1, total, w, h)
    return

with open('./day10/input.txt', 'r') as f:
    ans1 = 0
    grid = [[int(x) for x in line] for line in f.read().split('\n')]
    w = len(grid[0])
    h = len(grid)
    for j in range(h):
        for i in range(w):
            if grid[j][i] != 0:
                continue
            seen = [False for _ in range(w*h)]
            find_next(grid, i, j, seen, w, h)
            ans1 += sum(seen)
    print(ans1)
    
    ans2 = 0
    for j in range(h):
        for i in range(w):
            if grid[j][i] != 0:
                continue
            total = [0]
            find_next2(grid, i, j, total, w, h)
            ans2 += total[0]
    print(ans2)

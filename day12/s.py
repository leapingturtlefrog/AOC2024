def calc(grid, seen, val, x, y, w, h, area, per):
    seen[x + y*w] = True
    area[0] += 1
    next = []
    if x > 0 and grid[y][x - 1] == val:
        next += [[x - 1, y]]
    if x < w - 1 and grid[y][x + 1] == val:
        next += [[x + 1, y]]
    if y > 0 and grid[y - 1][x] == val:
        next += [[x, y - 1]]
    if y < h - 1 and grid[y + 1][x] == val:
        next += [[x, y + 1]]
    seen_adj = 0
    for loc in next:
        if seen[loc[0] + loc[1]*w]:
            seen_adj += 1
    per[0] += 4 - 2*seen_adj
    for loc in next:
        if not seen[loc[0] + loc[1]*w]:
            calc(grid, seen, val, loc[0], loc[1], w, h, area, per)

with open('./day12/input.txt', 'r') as f:
    ans1 = 0
    grid = f.read().split('\n')
    w = len(grid[0])
    h = len(grid)
    seen_global = [False for _ in range(w*h)]
    for j in range(h):
        for i in range(w):
            if not seen_global[i + j*w]:
                seen = [False for _ in range(w*h)]
                area = [0]
                per = [0]
                calc(grid, seen, grid[j][i], i, j, w, h, area, per)
                ans1 += area[0] * per[0]
                seen_global = [a or b for a, b in zip(seen_global, seen)]
    print(ans1)
    
    ans2 = 0
    
    print(ans2)

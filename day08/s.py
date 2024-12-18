with open('./day08/input.txt', 'r') as f:
    ans1 = 0
    grid = f.read()
    true_width = grid.index('\n')
    width = true_width + 1
    height = len(grid) // width
    seen = [False for _ in range(len(grid))]
    for j in range(height):
        for i in range(true_width):
            loc = i + j*width
            spot = grid[i + j*width]
            if spot == '.':
                continue
            min_loc = loc
            new_loc = grid.find(spot, min_loc + 1)
            while new_loc != -1:
                x = new_loc % width
                y = new_loc // width
                dx = x - i
                dy = y - j
                nodeX = i - dx
                nodeY = j - dy
                if -1 < nodeX < true_width and -1 < nodeY < height:
                    seen[nodeX + nodeY*width] = True
                nodeX = x + dx
                nodeY = y + dy
                if -1 < nodeX < true_width and -1 < nodeY < height:
                    seen[nodeX + nodeY*width] = True
                min_loc = new_loc
                new_loc = grid.find(spot, min_loc + 1)
    ans1 = sum(seen)
    print(ans1)
    
    ans2 = 0
    seen = [False for _ in range(len(grid))]
    for j in range(height):
        for i in range(true_width):
            loc = i + j*width
            spot = grid[i + j*width]
            if spot == '.':
                continue
            min_loc = loc
            new_loc = grid.find(spot, min_loc + 1)
            while new_loc != -1:
                x = new_loc % width
                y = new_loc // width
                dx = x - i
                dy = y - j
                while True:
                    if -1 < x < true_width and -1 < y < height:
                        seen[x + y*width] = True
                    else:
                        break
                    x += dx
                    y += dy
                x = i
                y = j
                while True:
                    if -1 < x < true_width and -1 < y < height:
                        seen[x + y*width] = True
                    else:
                        break
                    x -= dx
                    y -= dy
                min_loc = new_loc
                new_loc = grid.find(spot, min_loc + 1)
    ans2 = sum(seen)
    print(ans2)

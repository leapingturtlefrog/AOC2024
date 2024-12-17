with open('./day6/input.txt', 'r') as f:
    locs = f.read()
    true_width = locs.index('\n')
    width = true_width + 1
    height = (len(locs) - 1) // true_width
    seen = [False for _ in range(len(locs))]
    og_curr = locs.index('^')
    curr = og_curr
    locs = locs[:curr] + '.' + locs[curr+1:]
    seen[curr] = True
    dir = [0, -1] # [dx, dy] on 2d map. 0, 0 top left
    while True:
        new_spot = curr + dir[0] + dir[1]*width
        if (new_spot + 1) % width == 0 or new_spot < 0 or new_spot > len(locs) - 1:
            break
        if locs[new_spot] == '.':
            seen[new_spot] = True
            curr = new_spot
        elif dir[0] == 0:
            dir = [-dir[1], 0]
        else:
            dir = [0, dir[0]]
    ans1 = sum(seen)
    print('Part 1:', ans1, '\n\nPart 2 tracker:') # part 1
    
    ans2 = 0
    for j in range(height):
        for i in range(true_width):
            spot = i + j*width
            if locs[spot] == '#' or spot == og_curr:
                continue
            curr = og_curr
            temp_locs = locs[:spot] + '#' + locs[spot+1:]
            traversed_list = [0 for _ in range(len(temp_locs))]
            dir = [0, -1]
            while True:
                new_spot = curr + dir[0] + dir[1]*width
                if (new_spot + 1) % width == 0 or new_spot < 0 or new_spot > len(temp_locs) - 1:
                    break
                elif traversed_list[new_spot] > 4:
                    ans2 += 1
                    print(ans2)
                    break
                if temp_locs[new_spot] == '.':
                    traversed_list[new_spot] += 1
                    curr = new_spot
                elif dir[0] == 0:
                    dir = [-dir[1], 0]
                else:
                    dir = [0, dir[0]]
    print('\nPart 1:', ans1)
    print('Part 2:', ans2) # part 2
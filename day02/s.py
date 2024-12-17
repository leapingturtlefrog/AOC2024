def count(lst):
    first = int(lst[0])
    prev = int(lst[1])
    if first < prev < first + 4:
        increasing = True
    elif first - 4 < prev < first:
        increasing = False
    else:
        return 0 # does not match pattern
    match = True
    for curr in lst[2:]:
        if increasing and prev < int(curr) < prev + 4:
            prev = int(curr)
        elif not increasing and prev - 4 < int(curr) < prev:
            prev = int(curr)
        else:
            match = False
            break
    if match == True:
        return 1
    else:
        return 0

with open('./day02/input.txt', 'r') as f:
    ans = 0
    for line in f:
        ans += count(line.split(' '))
    print(ans) # part 1
    f.seek(0)
    ans2 = 0
    for line in f:
        lst = line.split(' ')
        for i in range(len(lst)):
            if count(lst[:i] + lst[i+1:]) == 1:
                ans2 += 1
                break
    print(ans2) # part 2
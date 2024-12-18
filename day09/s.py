with open('./day09/input.txt', 'r') as f:
    ans1 = 0
    input_lst = [int(c) for c in f.read()]
    lst = []
    val = 0
    for i in range(len(input_lst)):
        if i % 2 == 0:
            lst += [val for _ in range(input_lst[i])]
            val += 1
        else:
            lst += [0 for _ in range(input_lst[i])]
    lst2 = lst.copy()
    l_pt = input_lst[0]
    r_pt = len(lst) - 1
    while l_pt < r_pt:
        if lst[l_pt] == 0:
            while lst[r_pt] == 0:
                r_pt -= 1
            lst[l_pt], lst[r_pt] = lst[r_pt], 0
            r_pt -= 1
        l_pt += 1
    ans1 = sum(pos * value for pos, value in enumerate(lst[:lst.index(0, input_lst[0])]))
    print(ans1)
    
    ans2 = 0
    min_pt = ll_pt = lr_pt = input_lst[0]
    while True:
        if lst2[lr_pt] == 0:
            lr_pt += 1
        else:
            break
    free_space = lr_pt - ll_pt + 1
    rr_pt = rl_pt = len(lst2) - 1
    while min_pt < rl_pt:
        while True:
            if lst2[rl_pt] == lst2[rr_pt]:
                rl_pt -= 1
            else:
                break
        space_needed = rr_pt - rl_pt + 1
        while free_space < space_needed and lr_pt < rl_pt:
            try:
                ll_pt = lst2.index(0, ll_pt + 1)
            except ValueError:
                break
            lr_pt = ll_pt
            while True:
                if lst2[lr_pt] == 0:
                    lr_pt += 1
                else:
                    break
            free_space = lr_pt - ll_pt + 1
            if free_space >= space_needed:
                for i in range(space_needed):
                    lst2[ll_pt + i], lst2[rr_pt - i] = lst2[rr_pt - i], 0
        ll_pt = lr_pt = min_pt = lst2.index(0, input_lst[0])
        while True:
            if lst2[lr_pt] == 0:
                lr_pt += 1
            else:
                break
        free_space = lr_pt - ll_pt + 1
        rr_pt = rl_pt - 1
        while True:
            if lst2[rr_pt] == 0:
                rr_pt -= 1
            else:
                break
        rl_pt = rr_pt
        print(lst2)
    ans2 = sum(pos * value for pos, value in enumerate(lst2))
    print(ans2)
    # 3113520244347 low
    # 6620308476548 high
    # 15603095437040 high
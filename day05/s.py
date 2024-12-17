with open('./day05/input.txt', 'r') as f:
    not_ordered_lst = []
    
    ans1 = 0
    sec1, sec2 = f.read().split('\n\n')
    lst1 = [int(x) for x in sec1.replace('\n', '|').split('|')]
    lst2 = sec2.split('\n')
    for line in lst2:
        ordered = True
        line_lst = [int(x) for x in line.split(',')]
        for i in range(len(lst1) // 2):
            try:
                if line_lst.index(lst1[i*2+1]) < line_lst.index(lst1[i*2]):
                    ordered = False
                    not_ordered_lst.append(line_lst)
                    break
            except ValueError:
                continue
        if ordered:
            ans1 += line_lst[(len(line_lst) - 1) // 2]
    print(ans1) # part 1
    
    ans2 = 0
    for line_lst in not_ordered_lst:
        comp_lst = []
        for i in range(len(lst1) // 2):
            if lst1[i*2] in line_lst and lst1[i*2+1] in line_lst:
                comp_lst.append(lst1[i*2])
                comp_lst.append(lst1[i*2+1])
        while True:
            ordered = True
            for i in range(len(comp_lst) // 2):
                idx1 = line_lst.index(comp_lst[i*2])
                idx2 = line_lst.index(comp_lst[i*2+1])
                if idx2 < idx1:
                    line_lst[idx2], line_lst[idx1] = line_lst[idx1], line_lst[idx2]
                    ordered = False
                    break
            if ordered:
                ans2 += line_lst[(len(line_lst) - 1) // 2]
                break
    print(ans2) # part 2
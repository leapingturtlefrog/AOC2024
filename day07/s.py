from functools import reduce

def get_ternary_ops(num):
    if num == 0:
        return [0]
    res = []
    while num:
        res.append(num % 3)
        num //= 3
    return res[::-1]
    
def concat(num1, num2):
    return int(str(num1) + str(num2))

with open('./day07/input.txt', 'r') as f:
    ans1 = 0
    for line in f:
        target, *lst = [int(x) for x in line.replace(':', '', 1).split(' ')]
        combs = 2**(len(lst) - 1)
        curr = combs
        num_of_ops = len(list(bin(curr - 1)[2:]))
        for i in range(combs):
            curr -= 1
            ops = list(bin(curr)[2:])
            ops = ['0' for i in range(num_of_ops - len(ops))] + ops
            if reduce(lambda res, j: res * lst[j+1] if ops[j] == '1' \
                    else res + lst[j+1], range(len(ops)), lst[0]) == target:
                ans1 += target
                break
    print(ans1)
    
    ans2 = 0
    f.seek(0)
    for line in f:
        target, *lst = [int(x) for x in line.replace(':', '', 1).split(' ')]
        combs = 3**(len(lst) - 1)
        curr = combs
        num_of_ops = len(get_ternary_ops(curr - 1))
        for i in range(combs):
            curr -= 1
            ops = get_ternary_ops(curr)
            ops = [0 for i in range(num_of_ops - len(ops))] + ops
            if reduce(lambda res, j: concat(res, lst[j+1]) if ops[j] == 2 \
                    else res * lst[j+1] if ops[j] == 1 \
                    else res + lst[j+1], range(len(ops)), lst[0]) == target:
                ans2 += target
                break
    print(ans2)

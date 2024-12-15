import re

def digits(num):
    if num // 100 > 0:
        return 3
    elif num // 10 > 0:
        return 2
    else:
        return 1

with open('./day3/input.txt', 'r') as f:
    ans = 0
    for part in f.read().split('mul('):
        try:
            first = int(re.match(r'\d+', part).group())
            d1 = digits(first)
            second = int(re.match(r'\d+', part[d1+1:]).group())
            if part[d1] == ',' and part[d1+digits(second)+1] == ')':
                ans += first * second
        except Exception:
            pass
    print(ans) # part 1
    
    f.seek(0)
    ans = 0
    cont = True
    for part in f.read().split('mul('):
        try:
            if cont:
                first = int(re.match(r'\d+', part).group())
                d1 = digits(first)
                second = int(re.match(r'\d+', part[d1+1:]).group())
                if part[d1] == ',' and part[d1+digits(second)+1] == ')':
                    ans += first * second
        except Exception:
            pass
        do = part.rfind('do()')
        dont = part.rfind("don't()")
        if do > dont:
            cont = True
        elif do < dont:
            cont = False
    print(ans) # part 2
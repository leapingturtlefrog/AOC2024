def add(d, key, val):
    d[key] = val + d.get(key, 0)

def calc(stones, iters):
    for _ in range(iters):
        new_stones ={'1': stones.get('0', 0)}
        stones.pop('0', 0)
        for key in list(stones.keys()):
            if len(key) % 2 == 0:
                add(new_stones, key[:len(key) // 2], stones[key])
                add(new_stones, str(int(key[len(key) // 2:])), stones[key])
            else:
                add(new_stones, str(int(key) * 2024), stones[key])
        stones = new_stones
    return sum(stones.values())

with open('./day11/input.txt', 'r') as f:
    dictionary = {key: 1 for key in f.read().split(' ')}
    ans1 = calc(dictionary.copy(), 25)
    print(ans1)
    ans2 = calc(dictionary, 75)
    print(ans2)

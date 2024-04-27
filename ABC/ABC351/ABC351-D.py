import sys
sys.setrecursionlimit(10**6)

H, W = map(int, input().split())
S_list = []
for _ in range(H):
    S_list.append(input())

bom_set = set()
magnet_set = set()

for h in range(H):
    for w in range(W):
        if S_list[h][w] == "#":
            bom_set.add((h, w))
            if h-1>=0:
                magnet_set.add((h-1, w))
            if h+1<=H-1:
                magnet_set.add((h+1, w))
            if w-1>=0:
                magnet_set.add((h, w-1))
            if w+1<=W-1:
                magnet_set.add((h, w+1))

already_check_set = set()

max_value = 0

def f(h, w, sum_value):
    global max_value
    if sum_value > max_value:
        max_value = sum_value

    if (h, w) in already_check_set:
        return
        
    temp_score = 0
    if (h-1, w) in magnet_set:
        temp_score += 1
    if (h+1, w) in magnet_set:
        temp_score += 1
    if (h, w-1) in magnet_set:
        temp_score += 1
    if (h, w+1) in magnet_set:
        temp_score += 1

    already_check_set.add((h, w))
        
    if (h-1, w) not in magnet_set:
        f(h-1, w, temp_score)
    if (h+1, w) not in magnet_set:
        f(h+1, w, temp_score)
    if (h, w-1) not in magnet_set:
        f(h, w-1, temp_score)
    if (h, w+1) not in magnet_set:
        f(h, w+1, temp_score)



for h in range(H):
    for w in range(W):
        if (h, w) in bom_set or (h, w) in magnet_set:
            continue
        if (h, w) in already_check_set:
            continue

        temp_score = 0
        if (h-1, w) in magnet_set:
            temp_score += 1
        if (h+1, w) in magnet_set:
            temp_score += 1
        if (h, w-1) in magnet_set:
            temp_score += 1
        if (h, w+1) in magnet_set:
            temp_score += 1

        already_check_set.add((h, w))
        
        if (h-1, w) not in magnet_set:
            f(h-1, w, temp_score)
        if (h+1, w) not in magnet_set:
            f(h+1, w, temp_score)
        if (h, w-1) not in magnet_set:
            f(h, w-1, temp_score)
        if (h, w+1) not in magnet_set:
            f(h, w+1, temp_score)

print(max_value)

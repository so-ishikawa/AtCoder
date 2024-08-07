import sys
sys.setrecursionlimit(10**6)

H, W = map(int, input().split())
S_list = []
for _ in range(H):
    S_list.append(input())

magnet_set = set()
forced_set = set()
free_set = set()

for h in range(H):
    for w in range(W):
        if S_list[h][w] != "#":
            continue
        magnet_set.add((h, w))
        if h-1>=0:
            forced_set.add((h-1, w))
        if h+1<=H-1:
            forced_set.add((h+1, w))
        if w-1>=0:
            forced_set.add((h, w-1))
        if w+1<=W-1:
            forced_set.add((h, w+1))

temp_free_set = set()
for h in range(H):
    for w in range(W):
        temp_free_set.add((h, w))

free_set = temp_free_set - magnet_set - forced_set

checked_free_set = set()

def f(h, w, sum_score, checked_forced_set):
    global checked_free_set
    global forced_set
    global magnet_set
    if (h, w) in forced_set:
        if (h, w) in checked_forced_set:
            return(sum_score)
        # print((h, w))
        checked_forced_set.add((h, w))
        return(sum_score+1)

    # free
    if (h, w) in checked_free_set:
        return(sum_score)
    # print((h, w))
    checked_free_set.add((h, w))
    sum_score += 1
    
    if h-1 >= 0 and (h-1, w) not in magnet_set:
        sum_score = f(h-1, w, sum_score, checked_forced_set)
    if h+1 <= H-1 and (h+1, w) not in magnet_set:
        sum_score = f(h+1, w, sum_score, checked_forced_set)
    if w-1 >= 0 and (h, w-1) not in magnet_set:
        sum_score = f(h, w-1, sum_score, checked_forced_set)
    if w+1 <= W-1 and (h, w+1) not in magnet_set:
        sum_score = f(h, w+1, sum_score, checked_forced_set)  
    return(sum_score)

highest_score = 0

for h in range(H):
    for w in range(W):
        if (h, w) in magnet_set:
            continue
        if (h, w) in forced_set:
            if highest_score < 1:
                highest_score = 1
            continue
        if (h, w) in checked_free_set:
            continue
        
        # print((h, w))
        score = 1
        _checked_forced_set = set()
        checked_free_set.add((h, w))
        
        if h-1 >= 0:
            score = f(h-1, w, score, _checked_forced_set)
        if h+1 <= H-1:
            score = f(h+1, w, score, _checked_forced_set)
        if w-1 >= 0:
            score = f(h, w-1, score, _checked_forced_set)
        if w+1 <= W-1:
            score = f(h, w+1, score, _checked_forced_set)

        if score > highest_score:
            highest_score = score
        # print("----------")
print(highest_score)


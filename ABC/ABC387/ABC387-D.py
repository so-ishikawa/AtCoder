import sys
sys.setrecursionlimit(20000000)

H, W = map(int, input().split())
S_list = []
S = None
G = None
for h in range(H):
    temp = input()
    if "S" in temp:
        S = (h, temp.index("S"))
    if "G" in temp:
        G = (h, temp.index("G"))
    S_list.append(temp)

H_passed_set = set()
H_current_set = set()
W_passed_set = set()
W_current_set = set()

min_count = 9999999999

def f(isH, passed_set, current_set, count):
    global min_count

    if count > min_count:
        return
    
    if G in current_set:
        if min_count > count:
            min_count = count
        return
        
    if isH:
        temp = set()
        for i in current_set:
            y, x = i
            if y - 1 >= 0 and S_list[y-1][x] != "#" and (y-1, x) not in passed_set:
                temp.add((y-1, x))
            if y + 1 < H and S_list[y+1][x] != "#" and (y+1, x) not in passed_set:
                temp.add((y+1, x))
        if len(temp) == 0:
            return
        passed_set |= current_set
        current_set = temp
        f(not isH, passed_set, current_set, count+1)
    else:
        temp = set()
        for i in current_set:
            y, x = i
            if x - 1 >= 0 and S_list[y][x-1] != "#" and (y, x-1) not in passed_set:
                temp.add((y, x-1))
            if x + 1 < W and S_list[y][x+1] != "#" and (y, x+1) not in passed_set:
                temp.add((y, x+1))
        if len(temp) == 0:
            return
        passed_set |= current_set
        current_set = temp
        f(not isH, passed_set, current_set, count+1)

H_current_set.add(S)
W_current_set.add(S)
f(True, H_passed_set, H_current_set, 0)
f(False,W_passed_set, W_current_set, 0)

if min_count == 9999999999:
    print(-1)
    exit()
print(min_count)

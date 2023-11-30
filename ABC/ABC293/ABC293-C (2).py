import copy
H, W = map(int, input().split())
A_list = []
for i in range(H):
    a = list(map(int, input().split()))
    A_list.append(a)

    
temp_set = set({A_list[0][0]})
count = 0

def f(_set, h, w):
    # print(h,w)
    global count
    current_num = A_list[h-1][w-1]
    if current_num in _set:
        return
    if h == H and w == W:
        # print(_set)
        count += 1
        return
    _set.add(current_num)
    if h+1<=H:
        f(_set.copy(), h+1,w)
    if w+1<=W:
        f(_set.copy(), h,w+1)

f(temp_set.copy(),2,1)
f(temp_set.copy(),1,2)

print(count)

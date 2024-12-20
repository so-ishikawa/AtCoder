N = int(input())

LR_list = []
_min = 0
_max = 0
_sum = 0
for i in range(N):
    L, R = map(int, input().split())
    LR_list.append([L, R, R])
    _min += L
    _max += R
    _sum += R
    
if _min > 0 or 0 > _max:
    print("No")
    exit()


for i in LR_list:
    if _sum == 0:
        break

    if _sum - i[1] + i[0] > 0:
        i[2] = i[0]
        _sum = _sum - i[1] + i[0]
        continue

    i[2] = i[1] - _sum
    _sum = 0

print("Yes")
for i in LR_list:
    print(i[2], end=" ")

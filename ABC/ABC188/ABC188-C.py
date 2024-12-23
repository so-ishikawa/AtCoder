N = int(input())
A_list = list(map(int, input().split()))

if len(A_list) == 2:
    print(2 if A_list[0] > A_list[1] else 1)
    exit()


flag = True
target = A_list.copy()
temp = []
for i in range(0, len(target), 2):
    temp.append(max((target[i], i+1),(target[i+1], i+2)))


while len(temp) > 2:
    _temp = []
    for i in range(0, len(temp), 2):
        _temp.append(max(temp[i],temp[i+1]))
    temp.clear()
    temp = _temp

print(min(temp[0], temp[1])[1])
    
    

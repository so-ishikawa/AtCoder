N = int(input())

A_list = ["dummy"]
dic = dict()

temp = [None]*N
temp.insert(0, "dummy")

for i in range(N):
    a, b, x = map(int, input().split())
    A_list.append(a)
    if x in dic:
        dic[x].append((i+1, b))
    else:
        dic[x] = [(i+1, b)]

for i in range(1, N+1):
    if i == 1:
        temp[1] = 0
        continue
    _list = []
    a = temp[i-1] + A_list[i-1]
    _list.append(a)
    for j in dic[i]:
        target = j[0]
        value = j[1]
        if target > i:
            continue
        b = temp[target] + value
        _list.append(b)
    temp[i] = min(_list)
print(temp)

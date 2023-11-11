N = int(input())
D_list = list(map(int, input().split()))

D_list.insert(0, "dummy")

zoro_count = 0
for i in range(1, N+1):
    if len(set(list(str(i)))) != 1:
        continue
    for j in range(1, 3+1):
        if D_list[i] >= int(list(set(list(str(i))))[0] * j):
            # print(i,  int(list(set(list(str(i))))[0] * j))
            zoro_count += 1

print(zoro_count)

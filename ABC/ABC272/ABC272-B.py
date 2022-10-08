N, M = map(int, input().split())
k_list = []
n_list = []

for i in range(M):
    temp = list(map(int, input().split()))
    # temp.sort()
    k_list.append(temp[1:])

for i in range(N):
    n_list.append([])

for i in range(len(k_list)):
    for k in k_list[i]:
        n_list[k-1].append(i)

flag = False
for i in range(len(n_list)):
    for j in range(i, len(n_list)):
        if i == j:
            continue
        if not (set(n_list[i]) & set(n_list[j])):
            print("No")
            flag = True
            break
    if flag:
        break

if not flag:
    print("Yes")

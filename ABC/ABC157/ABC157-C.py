N, M = map(int, input().split())
sc_list = []

result_list = [-1]*N
result_list.insert(0, "dummy")

for i in range(M):
    s, c = map(int, input().split())
    sc_list.append((s,c))

for i in sc_list:
    if result_list[i[0]] == -1:
        result_list[i[0]] = i[1]
        continue

    if result_list[i[0]] == i[1]:
        continue

    print(-1)
    exit()

for i in range(1, N+1):
    if i == 1:
        if N == 1:
            if result_list[1] == -1:
                result_list[1] = 0
                break
            if result_list[1] == 0:
                break
        if result_list[1] == 0:
            print(-1)
            exit()
        if result_list[1] == -1:
            result_list[1] = 1
            continue

    if result_list[i] == -1:
        result_list[i] = 0

result_list.pop(0)
print(int("".join([str(x) for x in result_list])))


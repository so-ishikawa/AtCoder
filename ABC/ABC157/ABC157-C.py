N, M = map(int, input().split())
sc_list = []
result_list = ["dummy", -1, -1, -1]
# flag_list = ["dummy", False, False, False]

for i in range(M):
    s, c = map(int, input().split())
    sc_list.append((s,c))

for i in sc_list:
    if result_list[i[0]] == -1:
        result_list[i[0]] = i[1]
        continue

    if result_list[i[0]] != i[1]:
        print(-1)
        exit()
    

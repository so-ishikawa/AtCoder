N = int(input())

s_list = []
for i in range(N):
    # s_list.append(list(map(str, input().split())))
    s_list.append(input())

result = []
for i in range(N):
    result.append([None]*N)

for h in range(N):
    for w in range(N):
        # print(N, w, N-w)
        result[h][N-w-1] = s_list[w][h]

for h in range(N):
    for w in range(N):
        print(result[h][w], end="")
    print("")



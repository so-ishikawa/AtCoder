N, M = map(int, input().split())
ab_list = []
cd_list = []
for i in range(N):
    a, b = map(int, input().split())
    ab_list.append((a, b))

for i in range(M):
    c, d = map(int, input().split())
    cd_list.append((c, d))

for n in range(N):
    min_length = 99999999999999999999
    min_num = -1
    for m in range(M):
        temp = abs(ab_list[n][0] - cd_list[m][0]) + abs(ab_list[n][1] - cd_list[m][1])
        if min_length > temp:
            min_length = temp
            min_num = m + 1
    print(min_num)
    

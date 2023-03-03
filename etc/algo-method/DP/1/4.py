import sys
N = int(input())

tile = [0]*(100)

current_index = 0

tile[1] = 1
tile[2] = 2
tile[3] = 4
if N<=3:
    print(tile[N])
    sys.exit(0)

for i in range(N+1):
    if i<=3:
        continue
    # print(i)
    tile[i] = tile[i-1] + tile[i-2] + tile[i-3]
    if i == N:
        print(tile[N])

N = int(input())
S_list = []
for i in range(N):
    S = input()
    S_list.append(S)


masu = []
for i in range(N):
    masu.append([0]*N)


#横軸
masu[0][0] = 1
for i in range(1, N):
    if S_list[0][i] == "#":
        masu[0][i] = 0
        continue
    masu[0][i] = masu[0][i-1]

#縦軸
for i in range(1, N):
    if S_list[i][0] == "#":
        masu[i][0] = 0
        continue
    masu[i][0] = masu[i-1][0]


for i in range(1, N):
    for j in range(1, N):
        if S_list[i][j] == "#":
            masu[i][j] = 0
            continue
        masu[i][j] = masu[i][j-1] + masu[i-1][j]


# 出力
"""
for i in range(N):
    for j in range(N):
        print(masu[i][j], end=" ")
    print("")
print("--------------")
"""
print(masu[N-1][N-1])

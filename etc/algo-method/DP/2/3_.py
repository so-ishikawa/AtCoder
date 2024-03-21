N = int(input())
A_list = []
for i in range(N):
    A_list.append(list(map(int, input().split())))

masu = []
for i in range(N):
    masu.append([0]*3)

masu[0][0] = A_list[0][0]
masu[0][1] = A_list[0][1]
masu[0][2] = A_list[0][2]

for i in range(1, N):
    for j in range(3):
        if j == 0:
            masu[i][j] = A_list[i][j] + max(masu[i-1][1], masu[i-1][2])
            continue
        if j == 1:
            masu[i][j] = A_list[i][j] + max(masu[i-1][0], masu[i-1][2])
            continue
        else:
            masu[i][j] = A_list[i][j] + max(masu[i-1][0], masu[i-1][1])
            continue
print(max(masu[N-1][0], masu[N-1][1], masu[N-1][2]))
# print(masu)

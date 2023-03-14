N = int(input())
a_list = []
for i in range(N):
    a = list(map(int, input().split()))
    a_list.append(a)

masu = []
for i in range(N):
    masu.append([0]*N)


masu[0][0] = a_list[0][0]

# x-axis
for i in range(1, N):
    masu[0][i] = masu[0][i-1] + a_list[0][i]

for i in range(1, N):
    masu[i][0] = masu[i-1][0] + a_list[i][0]

# print(masu)

for i in range(1, N):
    for j in range(1, N):
        masu[i][j] = (masu[i-1][j] if masu[i-1][j] > masu[i][j-1] else masu[i][j-1]) + a_list[i][j]

print(masu[N-1][N-1])

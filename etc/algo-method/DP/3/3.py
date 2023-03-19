N,M = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

masu = []
for i in range(N):
    masu.append([False] * M)

# -1 line
masu[0][0] = 0

# 0 - N-1 line
for n in range(1, N):
    for m in range(M):





print(masu)

if not masu[N-1][M-1]:
    print(-1)
else:
    print(masu[N-1][M-1])

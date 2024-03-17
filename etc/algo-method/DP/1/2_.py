N = int(input())
A_list = list(map(int, input().split()))

masu = [None]*N
masu[0] = 0
masu[1] = A_list[1]

for i in range(2, N):
    masu[i] = min(masu[i-1]+A_list[i], masu[i-2]+2*A_list[i])

print(masu[-1])

N = int(input())

masu = [0]*(N+1)

masu[0] = 1
masu[1] = 1

for i in range(2, N+1):
    masu[i] = masu[i-1] + masu[i-2]

print(masu[-1])

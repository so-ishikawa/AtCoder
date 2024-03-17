N = int(input())

if N == 1:
    print(1)
    exit()
if N == 2:
    print(2)
    exit()
if N == 3:
    print(4)
    exit()

masu = [0]*N

masu[0] = 1
masu[1] = 2
masu[2] = 4

for i in range(3, N):
    masu[i] = masu[i-1] + masu[i-2] + masu[i-3]

print(masu[-1])

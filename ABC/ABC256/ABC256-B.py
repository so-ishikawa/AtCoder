N = int(input())
A_list = list(map(int, input().split()))

P = 0
masu = [False] * 4

for i in A_list:
    masu[0] = True
    for j in range(len(masu)-1,-1,-1):
        if not masu[j]:
            continue
        masu[j] = False
        if j + i >= len(masu):
            P += 1
            continue
        masu[j+i] = True
print(P)

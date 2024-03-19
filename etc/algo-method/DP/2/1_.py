A0, A1, A2, A3 = map(int, input().split())

masu = []
for i in range(4):
    masu.append([0]*4)

masu[0][0] = A0
masu[0][1] = A1
masu[0][2] = A2
masu[0][3] = A3

for h in range(1, 4):
    for w in range(4):
        temp = 0
        if h-1>=0 and w-1>=0:
            temp += masu[h-1][w-1]
        if h-1>=0:
            temp += masu[h-1][w]
        if h-1>=0 and w+1<4:
            temp += masu[h-1][w+1]
        masu[h][w] = temp
print(masu[3][3])

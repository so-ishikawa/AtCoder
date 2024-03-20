N = int(input())
A_list = list(map(int, input().split()))

masu = []
masu.append(A_list)

for i in range(len(A_list)-1):
    masu.append([0]*len(A_list))

for h in range(1, len(A_list)):
    for w in range(len(A_list)):
        temp = 0
        if h-1>=0 and w-1>=0:
            temp += masu[h-1][w-1]
        if h-1>=0:
            temp += masu[h-1][w]
        if h-1>=0 and w+1<len(A_list):
            temp += masu[h-1][w+1]
        masu[h][w] = temp%100

print(masu[len(A_list)-1][len(A_list)-1])


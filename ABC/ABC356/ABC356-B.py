N, M = map(int, input().split())
A_list = list(map(int, input().split()))
X_list = []
for i in range(N):
    temp = list(map(int, input().split()))
    X_list.append(temp)


for m in range(M):
    temp = 0
    for n in range(N):
        temp += X_list[n][m]
    if temp < A_list[m]:
        print("No")
        exit()

print("Yes")

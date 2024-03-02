N = int(input())
A_list = []
for n in range(N):
    A_list.append(list(map(int, input().split())))
# print(A_list)

for i in range(N):
    for j in range(N):
        if A_list[i][j] == 0:
            continue
        print(j+1, end=" ")
    print("")

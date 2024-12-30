N = int(input())
A_list = list(map(int, input().split()))

temp = [None]*N
for i in range(N):
    temp[i] = [A_list[i], i+1]

temp.sort(key=lambda x: x[0])

for i in range(len(temp)):
    print(temp[i][1], end=" ")

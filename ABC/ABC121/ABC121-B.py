N, M, C = map(int, input().split())
B_list = list(map(int, input().split()))
A_list = []
for _ in range(N):
    a_list = list(map(int, input().split()))
    A_list.append(a_list)

count = 0
for n in range(N):
    temp = 0
    for m in range(M):
        temp += A_list[n][m]*B_list[m]
    if temp + C > 0:
        count += 1
print(count)

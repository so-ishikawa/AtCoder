N, T = map(int, input().split())
A_list = []
for i in range(N):
    A_list.append(int(input()))

temp = 0
for i in range(N-1):
    if T > A_list[i+1] - A_list[i]:
        temp = temp + (A_list[i+1]-A_list[i])
    else:
        temp += T

temp += T

print(temp)

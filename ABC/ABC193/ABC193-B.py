N = int(input())
A_list = []
P_list = []
X_list = []

for i in range(N):
    a, p, x = map(int, input().split())
    A_list.append(a)
    P_list.append(p)
    X_list.append(x)

min_value = 9999999999999999999

for i in range(N):
    if X_list[i] - A_list[i] <= 0:
        continue
    if min_value > P_list[i]:
        min_value = P_list[i]

if min_value == 9999999999999999999:
    print(-1)
    exit()

print(min_value)

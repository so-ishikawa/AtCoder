import bisect
N, X = map(int, input().split())
V_list = []
P_list = []

for i in range(N):
    v, p = map(int, input().split())
    V_list.append(v)
    P_list.append(p)

X100 = X * 100

flag = False
sum_alc = 0
for i in range(N):
    sum_alc += V_list[i]*P_list[i]
    if sum_alc > X100:
        print(i+1)
        exit()
print(-1)

N = int(input())
T_list = []
V_list = []

for i in range(N):
    t, v = map(int, input().split())
    T_list.append(t)
    V_list.append(v)

remain = 0
for i in range(N):
    if i == 0:
        remain = V_list[i]
        continue
    remain = max(0, remain - (T_list[i]-T_list[i-1]))
    remain += V_list[i]

print(remain)

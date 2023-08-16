import bisect
N, X = map(int, input().split())
V_list = []
P_list = []
sum_list = []
temp = 0

for i in range(N):
    v, p = map(int, input().split())
    V_list.append(v)
    P_list.append(p)

for i in range(N):
    temp = temp + V_list[i] * (P_list[i])
    sum_list.append(temp)
sum_list.insert(0, 0)

if X > sum_list[-1]:
    print(-1)
    exit()
# print(sum_list)
ans = bisect.bisect_right(sum_list, X*100)
print(ans)

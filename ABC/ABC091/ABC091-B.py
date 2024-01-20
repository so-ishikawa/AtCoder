N = int(input())
s_list = []
for _ in range(N):
    s_list.append(input())
M = int(input())
t_list = []
for _ in range(M):
    t_list.append(input())

s_set = set(s_list)
max_value = -9999999

for s in s_set:
    temp = s_list.count(s) - t_list.count(s)
    if max_value < temp:
        max_value = temp

if max_value < 0:
    print(0)
    exit()
print(max_value)

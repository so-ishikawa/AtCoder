N, C = map(int, input().split())
T_list = list(map(int, input().split()))
count = 0
last_time = 0
for i in range(len(T_list)):
    if i == 0:
        count += 1
        last_time = T_list[i]
        continue

    if T_list[i] - last_time >= C:
        last_time = T_list[i]
        count += 1
        continue

print(count)
        

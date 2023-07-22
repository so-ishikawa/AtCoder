N, D = map(int, input().split())
S_list = []
for i in range(N):
    S_list.append(input())

current_holiday = 0
max_holiday = 0
for i in range(D):#day
    temp_set = set()
    for j in range(N):#person
        temp_set.add(S_list[j][i])
    if len(temp_set) == 1 and temp_set == set({"o"}):
        current_holiday += 1
        if max_holiday < current_holiday:
            max_holiday = current_holiday
    else:
        current_holiday = 0

print(max_holiday)

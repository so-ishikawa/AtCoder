N = int(input())
A_list = []
for i in range(N):
    temp_ = list(map(int, input().split()))
    A_list.append(temp_)

result = [] * N

for i in range(N):
    if i == 0:
        result.append(A_list[0])
        continue
    temp = []
    for current_index in range(3):
        option_list = []
        for prev_index in range(3):
            if current_index == prev_index:
                continue
            option_list.append(result[i-1][prev_index] + A_list[i][current_index])
        temp.append(max(option_list))
        # print(i, current_index, option_list)
    result.append(temp)

print(max(result[N-1]))

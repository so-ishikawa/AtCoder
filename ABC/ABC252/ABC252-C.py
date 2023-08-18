N = int(input())
S_list = []
for i in range(N):
    S_list.append(input())

min_time = 9999999999999999999999999
for i in range(9+1):
    temp_max_time = 0
    temp_dic = dict()
    for s in S_list:
        for j in range(9+1):
            if s[j] == str(i):
                if i not in temp_dic:
                    temp_dic[j] = 1
                    temp_max_time = max(j, temp_max_time)
                    break
                temp_max_time = max(temp_max_time, j + temp_dic[i]*10)
                temp_dic[i] = temp_dic[i] + 1
                break
    # print(i, temp_max_time)
    if temp_max_time < min_time:
        min_time = temp_max_time
    # print()
print(min_time)
                

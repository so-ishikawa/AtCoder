N, Q = map(int, input().split())
S = input()
l_r_list = []
for i in range(Q):
    l, r = map(int, input().split())
    l_r_list.append((l, r))

flag_list = [0]*len(S)
for i in range(len(S)-1):
    if S[i] == S[i+1]:
        flag_list[i] = 1
    # else:
    #    flag_list[i] = 0

flag_list.insert(0, 0)
# print(flag_list)

sum_flag_list = [0]*(len(S)+1)
sum_temp = 0
for i in range(len(flag_list)):
    sum_temp += flag_list[i]
    sum_flag_list[i] = sum_temp

# print(sum_flag_list)

for i in l_r_list:
    print(sum_flag_list[i[1]-1] - sum_flag_list[i[0]-1])


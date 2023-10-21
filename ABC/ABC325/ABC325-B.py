N = int(input())
W_list = []
X_list = []
for i in range(N):
    w, x = map(int, input().split())
    W_list.append(w)
    X_list.append(x)


# if 

max_member_num = 0
for i in range(24):
    temp_member_num = 0
    for n in range(N):

        end_time = (i+X_list[n]) % 24
        # if i == 4:
        #     print(i+X_list[n], n)
        if 9 <= end_time and end_time <= 17:
            temp_member_num += W_list[n]
            # if temp_member_num == 1000001:
            #     print(i)
    if max_member_num < temp_member_num:
        max_member_num = temp_member_num
    # print(max_member_num)

print(max_member_num)

N = int(input())
AC_list = []
for i in range(N):
    A, C = map(int, input().split())
    AC_list.append((A, C, i+1))

flag_list = [True]*N
flag_list.insert(0, False)

AC_list.sort(key=lambda x: x[0], reverse=True)
checked_min_value = 99999999999999

for base_num in range(N-1):
    # """
    if AC_list[base_num][1] > checked_min_value:
        # print(checked_min_value)
        continue
    checked_min_value = AC_list[base_num][1]
    print(checked_min_value)
    # """
    for target_num in range(base_num+1, N):
        if not flag_list[target_num]:
            continue
        if AC_list[base_num][1] < AC_list[target_num][1]:
            flag_list[AC_list[target_num][2]] = False

print(flag_list.count(True))
for i in range(N+1):
    if i == 0:
        continue
    if flag_list[i] == True:
        print(i, end=" ")

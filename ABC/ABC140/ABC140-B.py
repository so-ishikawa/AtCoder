N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
C_list = list(map(int, input().split()))

A_list.insert(0, "dummy")
B_list.insert(0, "dummy")
C_list.insert(0, "dummy")

sum_value = 0
privious_menu_num = 999

for index in range(1, len(A_list)):
    current_menu_num = A_list[index]
    sum_value += B_list[current_menu_num]
    # print(sum_value, B_list[A_list[current_menu_num]])
    if current_menu_num - privious_menu_num == 1:
        sum_value += C_list[privious_menu_num]
    privious_menu_num = current_menu_num

print(sum_value)

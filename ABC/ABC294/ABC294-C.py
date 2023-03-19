N, M = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_result_list = []
b_result_list = []

a_current_index = 0
b_current_index = 0

for i in range(1, len(a_list)+len(b_list)+1):
    if a_current_index == len(a_list):
        b_current_index += 1
        b_result_list.append(i)
        continue
    if b_current_index == len(b_list):
        a_current_index += 1
        a_result_list.append(i)
        continue

    if a_list[a_current_index] < b_list[b_current_index]:
        a_current_index += 1
        a_result_list.append(i)
        continue

    b_current_index += 1
    b_result_list.append(i)


for i in a_result_list:
    print(i, end=" ")
print("")
for i in b_result_list:
    print(i, end=" ")

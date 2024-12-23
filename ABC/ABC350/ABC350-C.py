N = int(input())
A_list = list(map(int, input().split()))
A_list.insert(0, "dummy")

value_to_index_dic = dict()

for i in range(1, N+1):
    value_to_index_dic[A_list[i]] = i

swap_list = []
    
for current_index in range(1, N+1):
    if current_index == A_list[current_index]:
        continue
    target_index = value_to_index_dic[current_index]

    current_value = A_list[current_index]
    target_value = A_list[target_index]
    
    A_list[current_index], A_list[target_index] = A_list[target_index], A_list[current_index]
    swap_list.append((current_index, target_index))

    value_to_index_dic[current_value] = target_index
    value_to_index_dic[target_value] = current_index
    

print(len(swap_list))
for i in swap_list:
    print(i[0], i[1])

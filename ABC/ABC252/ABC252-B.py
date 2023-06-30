N, K = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_sort_list = []
for i in range(len(A_list)):
    A_sort_list.append((i+1, A_list[i]))
A_sort_list.sort(key=lambda x: x[1], reverse=True)
max_value = A_sort_list[0][1]

max_value_pair_set = set([x[0] for x in A_sort_list if x[1] == max_value])
B_set = set(B_list)

if len(max_value_pair_set & B_set) == 0:
    print("No")
    exit()
print("Yes")
exit()


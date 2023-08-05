N = int(input())
P_list = list(map(int, input().split()))

max_value = max(P_list)
max_index = P_list.index(max_value)

if max_index == 0:
    if P_list.count(max_value) != 1:
        print(1)
        exit()
    print(0)
    exit()

print(max_value - P_list[0] + 1)

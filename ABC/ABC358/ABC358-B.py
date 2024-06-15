N, A = map(int, input().split())
T_list = list(map(int, input().split()))

current = 0
for t_index in range(len(T_list)):
    if current == 0:
        print(T_list[t_index]+A)
        current = T_list[t_index]+A
        continue
    if current < T_list[t_index]:
        print(T_list[t_index]+A)
        current = T_list[t_index] + A
        continue
    print(current + A)
    current = current + A


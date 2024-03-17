N, C = map(int, input().split())
A_list = list(map(int, input().split()))

if C > 0:
    max_value = 0
    max_start_index = -1
    max_end_index = -1

    current_sum = 0
    start_index = -1

    for i in range(N):
        current_sum += A_list[i]
        if current_sum > max_value:
            max_value = current_sum
            max_start_index = start_index
            max_end_index = i
        if current_sum < 0:
            current_sum = 0
            start_index = i

    if max_value <= 0:
        print(sum(A_list))
    else:
        result = sum(A_list[:max_start_index+1]) + sum(A_list[max_start_index+1:max_end_index+1])*C + sum(A_list[max_end_index+1:])
        print(result)

else:
    min_value = float('inf')
    min_start_index = -1
    min_end_index = -1

    current_sum = 0
    start_index = -1

    for i in range(N):
        current_sum += A_list[i]
        if current_sum < min_value:
            min_value = current_sum
            min_start_index = start_index
            min_end_index = i
        if current_sum > 0:
            current_sum = 0
            start_index = i

    if min_value >= 0:
        print(sum(A_list))
    else:
        result = sum(A_list[:min_start_index+1]) + sum(A_list[min_start_index+1:min_end_index+1])*C + sum(A_list[min_end_index+1:])
        print(result)

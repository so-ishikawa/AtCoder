N, C = map(int, input().split())
A_list = list(map(int, input().split()))

tuple_list = [] #data

if C > 0:
    current_head = None
    current_sum = 0
    for a_index in range(len(A_list)):
        a = A_list[a_index]
        if a == 0:
            continue
        if current_head is None and a < 0:
            continue
        if current_head is not None and a < 0:
            current_sum += a
            continue
        if current_head is None and a > 0:
            current_head = a
            tuple_list.append((current_head, 0, a_index))
            continue
        if current_head is not None and a > 0:
            current_sum += a
            current_head = a
            tuple_list.append((current_head, current_sum, a_index))
            current_sum = 0
            continue

    # search max
    max_start_index = -1
    max_end_index = -1
    max_value = 0

    for start in range(len(tuple_list)):
        temp_value = tuple_list[start][0]
        for end in range(start, len(tuple_list)):
            if start != end:
                temp_value += tuple_list[end][1]
            if max_value < temp_value:
                max_value = temp_value
                max_start_index = tuple_list[start][2]
                max_end_index = tuple_list[end][2]

    if max_value == 0:
        print(sum(A_list))
        exit()

    temp = sum(A_list[:max_start_index])
    temp += sum([n*C for n in A_list[max_start_index:max_end_index+1]])
    temp += sum(A_list[max_end_index+1:])
    print(temp)
    exit()


else:
    current_head = None
    current_sum = 0
    for a_index in range(len(A_list)):
        a = A_list[a_index]
        if a == 0:
            continue
        if current_head is None and a > 0:
            continue
        if current_head is not None and a > 0:
            current_sum += a
            continue
        if current_head is None and a < 0:
            current_head = a
            tuple_list.append((current_head, 0, a_index))
            continue
        if current_head is not None and a < 0:
            current_sum += a
            current_head = a
            tuple_list.append((current_head, current_sum, a_index))
            current_sum = 0
            continue

    # search max
    min_start_index = -1
    min_end_index = -1
    min_value = 9999999999999999999999999

    for start in range(len(tuple_list)):
        temp_value = tuple_list[start][0]
        for end in range(start, len(tuple_list)):
            if start != end:
                temp_value += tuple_list[end][1]
            if min_value > temp_value:
                min_value = temp_value
                min_start_index = tuple_list[start][2]
                min_end_index = tuple_list[end][2]

    if min_value == 9999999999999999999999999:
        print(sum(A_list))
        exit()

    temp = sum(A_list[:min_start_index])
    temp += sum([n*C for n in A_list[min_start_index:min_end_index+1]])
    temp += sum(A_list[min_end_index+1:])
    print(temp)
    exit()


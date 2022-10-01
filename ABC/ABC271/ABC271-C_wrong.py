N = int(input())
a_list = list(map(int, input().split()))
a_list.sort()
# a_list = list(set(a_list)).sort()


waste_count = 0
aa = len(a_list)
result_count = 0
a_list_size = len(a_list)

if N == 1:
    print(0)
else:
    for i in range(1, aa):
        if i in a_list:
            result_count = i
            if a_list.count(i) != 1:
                waste_count = waste_count + a_list.count(i) - 1
                a_list_size = a_list_size - (a_list.count(i) - 1)
            continue
        # non
        if waste_count >= 2:
            waste_count = waste_count - 2
            result_count = i
            continue
        if waste_count == 1:
            if a_list_size > i:
                waste_count = 0
                a_list_size = a_list_size - 1
                result_count = i
                continue
            else:
                break
        if waste_count == 0:
            if a_list_size - i >= 2:
                a_list_size = a_list_size - 2
                result_count = i
                continue
            else:
                break

    print(result_count)

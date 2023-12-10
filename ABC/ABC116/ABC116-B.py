s = int(input())

temp = s
result_set = set({s})
for i in range(2, 1000000):
    if temp % 2 == 0:
        temp = temp // 2
    else:
        temp = 3*temp + 1
    result_set.add(temp)
    # print(result_set)
    if i != len(result_set):
        print(i)
        exit()



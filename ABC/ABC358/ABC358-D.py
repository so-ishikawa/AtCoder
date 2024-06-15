import bisect
N, M = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_list.sort()
B_list.sort()

flag_list = [True]*N
sum_ = 0
last_index = 0
for i in B_list:
    index = bisect.bisect_left(A_list, i, last_index, len(A_list))
    if index == len(A_list):
        print(-1)
        exit()
    while True:
        if index == len(A_list):
            print(-1)
            exit()
        if flag_list[index]:
            break
        index += 1
    flag_list[index] = False
    last_index = index
    sum_ += A_list[index]
print(sum_)

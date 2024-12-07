import bisect

N, M = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

C_list = []
temp_min = 999999999999999999
for num in range(len(A_list)):
    a = A_list[num]
    if temp_min > a:
        temp_min = a
        C_list.append((a, num))

C_list.reverse()

first, second = zip(*C_list)

D_list = C_list
D_list.reverse()

for b in B_list:
    index = bisect.bisect_right(first, b)
    # print(index)
    index = len(C_list) - index
    if index >= len(C_list):
        print(-1)
        continue
    print(D_list[index][1]+1)
    # index = len(C_list)-index-1
    # print(C_list[index][1])

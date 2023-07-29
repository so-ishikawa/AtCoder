import bisect

N, M = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_list.sort()
B_list.sort()

temp = list(set(A_list) | set(B_list))
temp.sort()

for i in temp:
    a = bisect.bisect(A_list, i)
    b = bisect.bisect_left(B_list, i)
    b = len(B_list) - b
    if a>=b:
        print(i)
        exit()

    i = i + 1
    a = bisect.bisect(A_list, i)
    b = bisect.bisect_left(B_list, i)
    b = len(B_list) - b
    if a>=b:
        print(i)
        exit()

import bisect
N, Q = map(int, input().split())
A_list = list(map(int, input().split()))

A_list.sort()

for i in range(Q):
    x = int(input())
    index = bisect.bisect_left(A_list, x)
    print(len(A_list)-index)

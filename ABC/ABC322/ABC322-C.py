import bisect

N, M = map(int, input().split())
A_list = list(map(int, input().split()))
A_list.insert(0, -1)

A_set = set(A_list)

for i in range(1, N+1):
    if i in A_set:
        print(0)
        continue
    index = bisect.bisect(A_list, i)
    print(A_list[index] - i)

# —vÄŠwK indexü‚è‚É©M–³‚µ
import bisect

N = int(input())
A_list = list(map(int, input().split()))

A_list.sort()
count = 0

for i in range(N-1):
    index = bisect.bisect_left(A_list, 10**8-A_list[i])
    count += (N-max(i+1, index))
print(sum(A_list)*(N-1) - (10**8)*count)


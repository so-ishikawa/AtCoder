import bisect

N = int(input())
A_list = list(map(int, input().split()))

A_list.sort()
_sum = []

for i in range(N-1):
    for j in range(i, N):
        _sum.append(A_list[i]+A_list[j]) 

count = 0

for i in range(N):
    index = bisect.bisect(A_list, 10**8-A_list[i])
    print("i:", i, " index:", index, " 10**8-A_list[i]:", 10**8-A_list[i])
    if index == N:
        continue
    if i >= index:
        break
    count += (N-index)
    
print(sum(A_list)*(N-1) - 10**8*count)


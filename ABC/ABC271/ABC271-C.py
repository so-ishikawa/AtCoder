from collections import deque

N = int(input())
a_list = list(map(int, input().split()))
check_set = set(a_list)

cost = 0

for i in range(1, N):
    if i in check_set:
        cost += 1
    else:
        cost += 2
    if cost > N:
        print(i-1)
        exit()
print(0)

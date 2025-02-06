from collections import deque

N = int(input())
a_list = list(map(int, input().split()))
a_list.sort()

d = deque(a_list)

index = 0
flag = False
for i in range(1, N):
    while d[index] < i and index < len(d):
        index += 1
    if index >= len(d):
        flag = True
    if d[index] == i:
        


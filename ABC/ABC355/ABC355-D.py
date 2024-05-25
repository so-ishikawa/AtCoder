"""
N = int(input())

temp = []
for _ in range(N):
    l, r = map(int, input().split())
    temp.append((l, r))

temp.sort()

count = 0

for s in range(len(temp)-1):
    s_end = temp[s][1]
    for t in range(s+1, len(temp)):
        t_start = temp[t][0]
        if s_end < t_start:
            break
        count += 1

print(count)
"""
import heapq

N = int(input())

intervals = []
for _ in range(N):
    l, r = map(int, input().split())
    intervals.append((l, r))


intervals.sort()

count = 0
end_heap = []

for l, r in intervals:

    while end_heap and end_heap[0] < l:
        heapq.heappop(end_heap)
    

    count += len(end_heap)
    

    heapq.heappush(end_heap, r)

print(count)

import bisect
N = int(input())

temp = []
for _ in range(N):
    l, r = map(int, input().split())
    temp.append((l, r))

temp.sort()
count = 0

for s in range(len(temp)-1):
    t = bisect.bisect(temp, temp[s][1], key=lambda i:i[0])
    count = count + t - s - 1

print(count)

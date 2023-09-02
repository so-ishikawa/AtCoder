N = int(input())
temp_set = set()
for i in range(N):
    a, b, c, d = map(int, input().split())
    for x in range(a+1, b+1):
        for y in range(c+1, d+1):
            temp_set.add((x, y))

print(len(temp_set))

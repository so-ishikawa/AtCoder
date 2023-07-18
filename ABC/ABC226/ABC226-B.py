N = int(input())
temp_set = set()

for _ in range(N):
    temp = list(map(int, input().split()))
    temp.pop(0)
    temp_set.add(tuple(temp))

print(len(temp_set))

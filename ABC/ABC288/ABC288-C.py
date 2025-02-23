N, M = map(int, input().split())
temp = set()
count = 0
for _ in range(M):
    A, B = map(int, input().split())
    if A in temp and B in temp:
        count += 1
        continue
    temp.add(A)
    temp.add(B)
print(count)

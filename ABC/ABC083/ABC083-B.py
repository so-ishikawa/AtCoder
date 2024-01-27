N, A, B = map(int, input().split())
count = 0
for i in range(1, N+1):
    temp = list(str(i))
    temp = [int(x) for x in temp]
    if A <= sum(temp) <= B:
        count += i
print(count)

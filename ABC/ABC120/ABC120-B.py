A, B, K = map(int, input().split())
count = 0

min_AB = min(A, B)
for i in range(min_AB, 0, -1):
    if A % i == 0 and B % i == 0:
        count += 1
        if count == K:
            print(i)

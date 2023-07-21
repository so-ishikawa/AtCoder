S, T = map(int, input().split())

count = 0
for a in range(S+1):
    for b in range(S+1):
        for c in range(S+1):
            if not (a + b + c <= S):
                continue
            if not (a * b * c <= T):
                continue
            count += 1
print(count)

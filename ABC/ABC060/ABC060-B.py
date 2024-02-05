A, B, C = map(int, input().split())

for i in range(99999999):
    if A * i % B == C:
        print("YES")
        exit()
print("NO")

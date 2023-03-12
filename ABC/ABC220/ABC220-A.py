A, B, C = map(int, input().split())
temp = B // C
if A <= temp * C:
    print(temp*C)
else:
    print(-1)

A, B = map(int, input().split())
range9x9 = list(range(1,10))
if A in range9x9 and B in range9x9:
    print(A*B)
else:
    print(-1)

A, B = map(int, input().split())
temp = A // B
if A % B == 0:
    print(temp)
else:
    print(A // B + 1)

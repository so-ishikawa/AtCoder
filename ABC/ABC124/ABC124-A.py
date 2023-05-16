A, B = map(int, input().split())

if A == B:
    print(2*A)
    exit()

print(max(A, B)*2-1)

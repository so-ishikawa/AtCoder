M, D = map(int, input().split())
y, m, d = map(int, input().split())

if M == m and D == d:
    print(y+1, 1, 1)
    exit()

if D == d:
    print(y, m+1, 1)
    exit()

print(y, m, d+1)

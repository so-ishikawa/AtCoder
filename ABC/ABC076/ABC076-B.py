N = int(input())
K = int(input())

temp = 1
for _ in range(N):
    a = temp * 2
    b = temp + K
    temp = min(a, b)
print(temp)

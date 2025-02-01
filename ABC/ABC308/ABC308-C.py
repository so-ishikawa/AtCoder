from decimal import Decimal

N = int(input())
result = []
X = 10**100
for i in range(N):
    A, B = map(int, input().split())
    result.append(((A*X)//(A+B),i+1))
    # result.append((A/(A+B), i+1))

result.sort(key=lambda x: (-x[0], x[1]))
for i in result:
    print(i[1], end=" ")

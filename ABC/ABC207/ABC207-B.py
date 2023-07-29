import math
A, B, C, D = map(int, input().split())

if C*D - B <= 0:
    print(-1)
    exit()

print(math.ceil(A/(C*D-B)))

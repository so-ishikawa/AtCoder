import math
N = int(input())
x = 0.0
y = 0.0
temp = 0.0
for i in range(N):
    _x, _y = map(int, input().split())
    temp += math.sqrt((x - _x)**2 + (y - _y)**2)
    x = _x
    y = _y
    if i == N-1:
        temp += math.sqrt(x**2 + y**2)
print(temp)

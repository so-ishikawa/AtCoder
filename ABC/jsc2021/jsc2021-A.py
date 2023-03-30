import math
X, Y, Z = map(int, input().split())
temp = Y*Z/X
x = math.modf(temp)
if x[0] == 0:
    print(int(temp - 1))
else:
    print(int(temp))

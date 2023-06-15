import math
a, b, d = map(int, input().split())
rad = math.radians(d)
x_ = math.cos(rad)*a + (-1*math.sin(rad)*b)
y_ = math.sin(rad)*a + math.cos(rad)*b

print(x_, y_)

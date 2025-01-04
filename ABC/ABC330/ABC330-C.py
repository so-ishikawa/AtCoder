D = int(input())

x = 0
while 2*x**2 < D:
    x += 1
x = x - 1
min_value = abs(D - 2*x**2)

y = x
while abs(D - x**2 - y**2) <= min_value:
    if y <= 0:
        break
    y -= 1

while abs(D - x**2 - y**2) <= min_value:
    x += 1
print(x, y)
print(abs(D-x**2-y**2))

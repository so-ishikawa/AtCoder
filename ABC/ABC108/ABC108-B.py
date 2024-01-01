x1, y1, x2, y2 = map(int, input().split())

temp_x4 = x2 - x1
temp_y4 = y2 - y1

x4 = -temp_y4 + x1
y4 = temp_x4 + y1

# print(x4, y4)

temp_x3 = x1 - x4
temp_y3 = y1 - y4

x3 = -temp_y3 + x4
y3 = temp_x3 + y4

print(x3, y3, x4, y4)


import sys

Y = int(input())
if Y % 4 == 0:
    y = Y + 2
elif Y % 4 == 1:
    y = Y + 1
elif Y % 4 == 2:
    y = Y
else:
    y = Y + 3
print(y)


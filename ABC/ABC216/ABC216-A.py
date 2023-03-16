import sys

X_Y = float(input())
X = int(X_Y)
Y = int(str(X_Y)[-1])

if 0<= Y and Y <= 2:
    print("%s-" % X)
    sys.exit(0)

if 3<= Y and Y <= 6:
    print(X)
    sys.exit(0)

if 7<= Y and Y <= 9:
    print("%s+" % X)
    sys.exit(0)

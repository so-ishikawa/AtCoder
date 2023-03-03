import sys
X, Y = map(int, input().split())

if X >= Y:
    print(0)
    sys.exit(0)

if (Y - X) % 10 == 0:
    print(int((Y-X) / 10))
    sys.exit(0)

print(int((Y - X) / 10) + 1)

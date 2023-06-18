x, a, b = map(int, input().split())

if abs(x - a) > abs(x - b):
    print("B")
    exit()

print("A")

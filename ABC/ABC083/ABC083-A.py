A, B, C, D = map(int, input().split())
L = A + B
R = C + D
if L > R:
    print("Left")
    exit()

if L < R:
    print("Right")
    exit()

print("Balanced")
exit()

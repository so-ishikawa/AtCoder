A, B, C, D = map(int, input().split())

while True:
    C = C - B
    if C <= 0:
        print("Yes")
        exit()
    A = A - D
    if A <= 0:
        print("No")
        exit()


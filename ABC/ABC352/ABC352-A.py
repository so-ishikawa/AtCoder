N, X, Y, Z = map(int, input().split())

if X > Y:
    if X > Z > Y:
        print("Yes")
    else:
        print("No")
    exit()

if Y > Z > X:
    print("Yes")
else:
    print("No")

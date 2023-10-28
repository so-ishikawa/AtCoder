X, Y = map(int, input().split())

if X > Y:
    if X - Y > 3:
        print("No")
        exit()
    print("Yes")
    exit()
else:# X < Y
    if Y - X > 2:
        print("No")
        exit()
    print("Yes")
    exit()
    

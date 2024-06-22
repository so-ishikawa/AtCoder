Sx, Sy = map(int, input().split())
Tx, Ty = map(int, input().split())

if Tx - Sx > 0:
    if Sy % 2 == 0 and Sx % 2 == 0:
        Sx += 1
    elif Sy % 2 == 1 and Sx % 2 == 1:
        Sx += 1
    if Ty % 2 == 0 and Tx % 2 == 1:
        Tx -= 1
    elif Ty % 2 == 1 and Tx % 2 == 0:
        Tx -= 1
    y_diff = abs(Ty - Sy)
    if Sx + y_diff >= Tx:
        print(y_diff)
        exit()
    x_diff = (Tx - (Sx + y_diff) + 1) // 2
    print(x_diff + y_diff)
    exit()
elif Tx - Sx < 0:
    if Sy % 2 == 0 and Sx % 2 == 1:
        Sx -= 1
    elif Sy % 2 == 1 and Sx % 2 == 0:
        Sx -= 1
    if Ty % 2 == 0 and Tx % 2 == 0:
        Tx += 1
    elif Ty % 2 == 1 and Tx % 2 == 1:
        Tx += 1
    y_diff = abs(Ty - Sy)
    if Sx - y_diff <= Tx:
        print(y_diff)
        exit()
    x_diff = abs(Tx - (Sx - y_diff) - 1) // 2
    print(x_diff + y_diff)
    exit()
else: #Tx - Sx = 0
    print(abs(Ty-Sy))
    exit()

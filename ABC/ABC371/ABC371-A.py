Sab, Sac, Sbc = map(str, input().split())

A = "A"
B = "B"
C = "C"

temp = []

if Sab == ">":
    temp.append(A)
    temp.append(B)
    if Sac == ">":
        if Sbc == ">":
            print("B")
            exit()
        else:
            print("C")
            exit()
    print("A")
    exit()
else:
    temp.append(B)
    temp.append(A)
    if Sac == ">":
        print("A")
        exit()
    else:
        if Sbc == ">":
            print("C")
            exit()
        else:
            print("B")
            exit()



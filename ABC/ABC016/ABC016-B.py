A, B, C = map(int, input().split())

plus = A + B
minus = A - B

A_plus_B = (plus == C)
A_minus_B = (minus == C)

if A_plus_B and A_minus_B:
    print("?")
    exit()

if not A_plus_B and not A_minus_B:
    print("!")
    exit()

if A_plus_B:
    print("+")
    exit()

if A_minus_B:
    print("-")
    exit()



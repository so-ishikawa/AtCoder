a, b = map(str, input().split())
if a == "H" and b == "H":
    print("H")
    exit()
if a == "H" and b == "D":
    print("D")
    exit()
if a == "D" and b == "H":
    print("D")
    exit()
if a == "D" and b == "D":
    print("H")
    exit()

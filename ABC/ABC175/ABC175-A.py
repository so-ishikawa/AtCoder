S = input()
if S[1] == "S":
    if "R" in S:
        print(1)
    else:
        print(0)
else:
    print(S.count("R"))

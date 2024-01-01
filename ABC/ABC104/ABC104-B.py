S = input()
if S[0] != "A":
    print("WA")
    exit()

if S[2:-1].count("C") != 1:
    print("WA")
    exit()

A_flag = False
C_flag = False

for i in S:
    if not A_flag and i=="A":
        A_flag = True
        continue
    if A_flag and i=="A":
        print("WA")
        exit()
    if not C_flag and i=="C":
        C_flag = True
        continue
    if C_flag and i=="C":
        print("WA")
        exit()
    if i.isupper():
        print("WA")
        exit()

print("AC")

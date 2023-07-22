N = int(input())
S = input()

flag_a = False
flag_b = False
flag_c = False

for j  in range(len(S)):
    i = S[j]
    if i == "A":
        flag_a = True
    if i == "B":
        flag_b = True
    if i == "C":
        flag_c = True
    if flag_a and flag_b and flag_c:
        print(j+1)
        exit()

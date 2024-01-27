S = input()
for i in range(len(S)):
    if i == 0:
        if not S[i].isupper():
            print("No")
            exit()
        continue
    if not S[i].islower():
        print("No")
        exit()
print("Yes")

S = input()

set_R = set({"R", "U", "D"})
set_L = set({"L", "U", "D"})

for i in range(len(S)):
    if i % 2 == 0:
        if S[i] not in set_R:
            print("No")
            exit()
        continue

    if S[i] not in set_L:
        print("No")
        exit()

print("Yes")
exit()

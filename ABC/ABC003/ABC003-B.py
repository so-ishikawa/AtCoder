S = input()
T = input()

set_ = set({"a","t","c","o","d","e","r","@"})

for i in range(len(S)):
    if S[i] == T[i]:
        continue
    
    if S[i] != "@" and T[i] != "@":
        print("You will lose")
        exit()

    if S[i] == "@":
        if T[i] not in set_:
            print("You will lose")
            exit()

    if T[i] == "@":
        if S[i] not in set_:
            print("You will lose")
            exit()

print("You can win")

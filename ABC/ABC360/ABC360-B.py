S, T = map(str, input().split())

for w in range(1, len(S)):
    splitted =  [S[i: i+w] for i in range(0, len(S), w)]
    for c in range(w+1):
        temp = ""
        for sp in splitted:
            if c >= len(sp):
                break
            temp = temp + sp[c]
        if temp == T:
            print("Yes")
            exit()

print("No")

H, W = map(int, input().split())

masu = []
h_except = []
w_except = []

for h in range(H):
    temp = input()
    if temp == "." * W:
        h_except.append(h)
    masu.append(temp)

for w in range(W):
    flag = False
    for h in range(H):
        if masu[h][w] == "#":
            flag = True
            break
    if flag:
        continue
    w_except.append(w)


for h in range(H):
    if h in h_except:
        continue
    for w in range(W):
        if w in w_except:
            continue
        print(masu[h][w], end="")
    print("")

    

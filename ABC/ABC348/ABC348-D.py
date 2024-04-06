H, W = map(int, input().split())

Grid = []
for h in range(H):
    Grid.append(input())

S_position = (-1, -1)
T_position = (-1, -1)

for h in range(H):
    for w in range(W):
        if Grid[h][w] == "S":
            S_position = (h, w)
            continue
        if Grid[h][w] == "T":
            T_position = (h, w)
            continue
            

N = int(input())

dic = dict()
for i in range(N):
    R, C, E = map(int, input().split())
    dic[(R-1, C-1)] = E
    
ban = []
for h in range(H):
    ban.append([None]*W)

if S_position not in dic:
    print("No")
    exit()

ban[S_position[0]][S_position[1]] = dic[S_position]


# first
for h in range(H):
    if h < S_position[0]:
        continue
    for w in range(W):
        if h == S_position[0] and w < S_position[1]:
            continue
        if Grid[h][w] == "#":
            continue
        if ban[h][w] == None:
            continue

        if h-1>=0:
            if Grid[h-1][w] == "#":
                pass
            elif (h-1, w) in dic:
                if ban[h-1][w] == None:
                    ban[h-1][w] = max(dic[(h-1,w)], ban[h][w]-1)
                else:
                    ban[h-1][w] = max(dic[(h-1,w)], ban[h][w]-1, ban[h-1][w])
            else:
                if ban[h-1][w] == None:
                    ban[h-1][w] = ban[h][w]-1
                else:
                    ban[h-1][w] = max(ban[h][w]-1, ban[h-1][w])
        if h+1<=H-1:
            if Grid[h+1][w] == "#":
                pass
            elif (h+1, w) in dic:
                if ban[h+1][w] == None:
                    ban[h+1][w] = max(dic[(h+1,w)], ban[h][w]-1)
                else:
                    ban[h+1][w] = max(dic[(h+1,w)], ban[h][w]-1, ban[h+1][w])
            else:
                if ban[h+1][w] == None:
                    ban[h+1][w] = ban[h][w]-1
                else:
                    ban[h+1][w] = max(ban[h][w]-1, ban[h+1][w]) 
        if w-1>=0:
            if Grid[h][w-1] == "#":
                pass
            elif (h, w-1) in dic:
                if ban[h][w-1] == None:
                    ban[h][w-1] = max(dic[(h,w-1)], ban[h][w]-1)
                else:
                    ban[h][w-1] = max(dic[(h,w-1)], ban[h][w]-1, ban[h][w-1])
            else:
                if ban[h][w-1] == None:
                    ban[h][w-1] = ban[h][w]-1
                else:
                    ban[h][w-1] = max(ban[h][w]-1, ban[h][w-1])
        if w+1<=W-1:
            if Grid[h][w+1] == "#":
                pass
            elif (h, w+1) in dic:
                if ban[h][w+1] == None:
                    ban[h][w+1] = max(dic[(h,w+1)], ban[h][w]-1)
                else:
                    ban[h][w+1] = max(dic[(h,w+1)], ban[h][w]-1, ban[h][w+1])
            else:
                if ban[h][w+1] == None:
                    ban[h][w+1] = ban[h][w]-1
                else:
                    ban[h][w+1] = max(ban[h][w]-1, ban[h][w+1])

#second
for h in range(H-1,-1,-1):
    # if h < S_position[0]:
    #     continue
    for w in range(W-1,-1,-1):
        # if h == S_position[0] and w < S_position[1]:
        #     continue
        if Grid[h][w] == "#":
            continue
        if ban[h][w] == None:
            continue

        if h-1>=0:
            if Grid[h-1][w] == "#":
                pass
            elif (h-1, w) in dic:
                if ban[h-1][w] == None:
                    ban[h-1][w] = max(dic[(h-1,w)], ban[h][w]-1)
                else:
                    ban[h-1][w] = max(dic[(h-1,w)], ban[h][w]-1, ban[h-1][w])
            else:
                if ban[h-1][w] == None:
                    ban[h-1][w] = ban[h][w]-1
                else:
                    ban[h-1][w] = max(ban[h][w]-1, ban[h-1][w])
        if h+1<=H-1:
            if Grid[h+1][w] == "#":
                pass
            elif (h+1, w) in dic:
                if ban[h+1][w] == None:
                    ban[h+1][w] = max(dic[(h+1,w)], ban[h][w]-1)
                else:
                    ban[h+1][w] = max(dic[(h+1,w)], ban[h][w]-1, ban[h+1][w])
            else:
                if ban[h+1][w] == None:
                    ban[h+1][w] = ban[h][w]-1
                else:
                    ban[h+1][w] = max(ban[h][w]-1, ban[h+1][w]) 
        if w-1>=0:
            if Grid[h][w-1] == "#":
                pass
            elif (h, w-1) in dic:
                if ban[h][w-1] == None:
                    ban[h][w-1] = max(dic[(h,w-1)], ban[h][w]-1)
                else:
                    ban[h][w-1] = max(dic[(h,w-1)], ban[h][w]-1, ban[h][w-1])
            else:
                if ban[h][w-1] == None:
                    ban[h][w-1] = ban[h][w]-1
                else:
                    ban[h][w-1] = max(ban[h][w]-1, ban[h][w-1])
        if w+1<=W-1:
            if Grid[h][w+1] == "#":
                pass
            elif (h, w+1) in dic:
                if ban[h][w+1] == None:
                    ban[h][w+1] = max(dic[(h,w+1)], ban[h][w]-1)
                else:
                    ban[h][w+1] = max(dic[(h,w+1)], ban[h][w]-1, ban[h][w+1])
            else:
                if ban[h][w+1] == None:
                    ban[h][w+1] = ban[h][w]-1
                else:
                    ban[h][w+1] = max(ban[h][w]-1, ban[h][w+1])
     




if ban[T_position[0]][T_position[1]] is not None:
    print("Yes")
    exit()
print("No")

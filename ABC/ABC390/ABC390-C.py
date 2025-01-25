H, W = map(int, input().split())
S_list = []
for i in range(H):
    S_list.append(input())

min_H = 9999999999999999999
min_W = 9999999999999999999
max_H = 0
max_W = 0

for h in range(H):
    for w in range(W):
        if S_list[h][w] == "#":
            if h < min_H:
                min_H = h
            if h > max_H:
                max_H = h
            if w < min_W:
                min_W = w
            if w > max_W:
                max_W = w

for h in range(min_H, max_H+1):
    for w in range(min_W, max_W+1):
        if S_list[h][w] == ".":
            print("No")
            exit()
print("Yes")
            

#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
H, W = map(int, input().split())
S_list = []
result = []

E_list = []
for h in range(H):
    S = input()
    if "E" in S:
        for i in range(len(S)):
            if S[i] == "E":
                E_list.append((h, i))

    S_list.append(S)
    result.append(list(S))
# print(result)
# exit()
if len(E_list) == 0:
    for h in range(H):
        print(S_list[h])
    exit()

last_add = E_list.copy()
temp = []

while len(last_add) != 0:
    for i in last_add:
        y = i[0]
        x = i[1]
        if y - 1 >= 0 and result[y-1][x] == ".":
            result[y-1][x] = "v"
            temp.append((y-1, x))
        if y + 1 <= H-1 and result[y+1][x] == ".":
            result[y+1][x] = "^"
            temp.append((y+1, x))
        if x - 1 >= 0 and result[y][x-1] == ".":
            result[y][x-1] = ">"
            temp.append((y, x-1))
        if x + 1 <= W-1 and result[y][x+1] == ".":
            result[y][x+1] = "<"
            temp.append((y, x+1))
    last_add = temp.copy()
    temp = []
    
#print(result)
# exit()

for h in range(H):
    for w in range(W):
        print(result[h][w], end="")
    print("")

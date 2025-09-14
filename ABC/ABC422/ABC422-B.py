#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

H, W = map(int, input().split())
stage = []
for _ in range(H):
    temp = input()
    stage.append(temp)

for h in range(H):
    for w in range(W):
        if stage[h][w] == ".":
            continue
        count = 0
        if h - 1 >= 0 and stage[h-1][w] == "#":
            count += 1
        if h + 1 < H and stage[h+1][w] == "#":
            count += 1
        if w - 1 >= 0 and stage[h][w-1] == "#":
            count += 1
        if w + 1 < W and stage[h][w+1] == "#":
            count += 1
        if not (count == 2 or count == 4):
            print("No")
            exit()
print("Yes")

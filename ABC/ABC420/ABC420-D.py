#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
import sys

sys.setrecursionlimit(9999999999999999999)
H, W = map(int, input().split())
grid = []
S = None
G = None
for h in range(H):
    temp = input()
    grid.append(temp)
    if "S" in temp:
        S = (h, temp.index("S"))
    if "G" in temp:
        G = (h, temp.index("G"))

# state = True # open/close
min_move = 99999999999999999999999

def f(h, w, _state, move_count, _passed):
    global min_move
    global grid
    if (h, w) == G:
        if move_count < min_move:
            min_move = move_count
        return
    if grid[h][w] == ".":
        pass
    if grid[h][w] == "o":
        pass
    if grid[h][w] == "x":
        pass
    if grid[h][w] == "?":
        _state = not _state

    if h-1 >= 0:
        if (h-1, w, _state) not in _passed:
            if ((_state and grid[h-1][w] != "x") or ((not _state) and grid[h-1][w] != "o")) and grid[h-1][w] != "#":
                temp = _passed.copy()
                temp.add((h-1, w, _state))
                f(h-1, w, _state, move_count+1, temp)
    if h+1 < H:
        if (h+1, w, _state) not in _passed:
            if ((_state and grid[h+1][w] != "x") or ((not _state) and grid[h+1][w] != "o")) and grid[h+1][w] != "#":
                temp = _passed.copy()
                temp.add((h+1, w, _state))
                f(h+1, w, _state, move_count+1, temp)
    if w-1 >= 0:
        if (h, w-1, _state) not in _passed:
            if ((_state and grid[h][w-1] != "x") or ((not _state) and grid[h][w-1] != "o")) and grid[h][w-1] != "#":
                temp = _passed.copy()
                temp.add((h, w-1, _state))
                f(h, w-1, _state, move_count+1, temp)
    if w+1 < W:
        if (h, w+1, _state) not in _passed:
            if ((_state and grid[h][w+1] != "x") or ((not _state) and grid[h][w+1] != "o")) and grid[h][w+1] != "#":
                temp = _passed.copy()
                temp.add((h, w+1, _state))
                f(h, w+1, _state, move_count+1, temp)


passed = set()
passed.add((S[0], S[1], True))

f(S[0], S[1], True, 0, passed.copy())
if min_move == 99999999999999999999999:
    print(-1)
    exit()
print(min_move)

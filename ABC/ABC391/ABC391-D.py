#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
from collections import deque

N, W = map(int, input().split())

max_dic = dict()

exist_list = [True]*N
exist_list.insert(0, "dummy")

grid = []
for _ in range(W):
    grid.append(deque())

block_list = []
for i in range(N):
    X, Y = map(int, input().split())
    X = X-1
    Y = Y-1
    block_list.append((i+1, X, Y))
    if X not in max_dic:
        max_dic[X] = Y
    else:
        if max_dic[X] < Y:
            max_dic[X] = Y

for k in max_dic.keys():
    for _ in range(max_dic[k]+1):
        grid[k].append(None)

for i in block_list:
    grid[i[1]][i[2]] = i[0]

for t in range(1, 2*(10**5)+1):
    change = False
    vanish_flag = True
    for i in range(W):
        if len(grid[i]) == 0:
            vanish_flag = False
            break
        if grid[i][0] is None:
            vanish_flag = False
            break
    if vanish_flag:
        change = True
        for i in range(W):
            name = grid[i].popleft()
            exist_list[name] = t
    for i in range(W):
        if len(grid[i]) == 0:
            continue
        if grid[i][0] is None:
            change = True
            grid[i].popleft()

    if not change:
        break

# print(exist_list)
Q = int(input())
for i in range(Q):
    T, A = map(int, input().split())
    if exist_list[A] is True:
        print("Yes")#, T, A, exist_list[A])
        continue
    if exist_list[A] > T+0.5:
        print("Yes")
        continue
    print("No")
        

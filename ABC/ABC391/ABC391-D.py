#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
from collections import deque

N, W = map(int, input().split())

max_dic = dict()

grid = [deque()] * W

block_list = []
for i in range(N):
    X, Y = map(int, input().split())
    X = X-1
    Y = Y-1
    block_list.append((X, Y))
    if X not in max_dic:
        max_dic[X] = Y
    else:
        if max_dic[X] < Y:
            max_dic[X] = Y
print(max_dic)
for k in max_dic.keys():
    grid[k].append([None]*max_dic[k])

print(grid)
    

#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())

N_list = []
for i in range(N):
    N_list.append(["."]*N)


for diff in range(0, N//2+1, 2):
    if N//2-diff < 0:
        break
    for i in range(diff, N-diff):
        for j in range(diff, N-diff):
            # for diff in [0, 2]: 
            if (i == diff or i == N-1-diff) or ( j == diff or j == N-1-diff):
                N_list[i][j] = "#"



for i in range(N):
    for j in range(N):
        print(N_list[i][j], end="")
    print("")

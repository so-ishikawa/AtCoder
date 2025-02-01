#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
import re

N, M = map(int, input().split())
S_list = []

for i in range(N):
    S_list.append(input())

T_list = []
for i in range(M):
    T_list.append(input())

diff = N - M
# print(diff)
for h_diff in range(diff+1):
    for w_diff in range(diff+1):
        flag = False
        for h in range(M):
            for w in range(M):
                # print(h_diff, w_diff, h, w)
                if h+h_diff >= N or w+w_diff>=N:
                    continue
                if T_list[h][w] != S_list[h+h_diff][w+w_diff]:
                    flag = True
                    break
            if flag:
                break
        # print(h_diff, w_diff)
        if flag:
            continue
        print(h_diff+1, w_diff+1)
        exit()
"""
result = []
for i in range(N):
    temp = [m.span()[0] for m in re.finditer(T_list[0], S_list[i])]
    for j in temp:
        result.append((i, j))

for i in result:
    flag = False
    for h in range(M):
        for w in range(M):
            if h+i[0]>=N or w+i[1]>=N:
                continue
            if T_list[h][w] != S_list[h+i[0]][w+i[1]]:
                flag = True
                break
        if flag:
            break
    if flag:
        continue
    print(i[0]+1,i[1]+1)
    exit()
"""

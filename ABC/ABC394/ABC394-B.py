#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
S_list = []
for i in range(N):
    S = input()
    S_list.append((len(S), S))

S_list.sort(key=lambda x: x[0])
temp = ""
for i in range(N):
    temp += S_list[i][1]
print(temp)

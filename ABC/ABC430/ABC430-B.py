#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

N, M = map(int,input().split())
S_list = []

for i in range(N):
    S_list.append(input())

set_ = set()
for i in range(N-M+1):
    for j in range(N-M+1):
        temp = []
        for mi in range(M):
            for mj in range(M):
                if S_list[i+mi][j+mj] == ".":
                    temp.append("0")
                else:
                    temp.append("1")
        set_.add(int("".join(temp)))
        # print(temp)

print(len(set_))
                
        

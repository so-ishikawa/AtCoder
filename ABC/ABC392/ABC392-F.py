#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

N = int(input())
P_list = list(map(int, input().split()))

temp = []
for p_index in range(len(P_list)):
    temp.append(P_list[p_index])
    
    for i in range(p_index):
        if temp[i] <= P_list[p_index]:
            temp[i] = temp[i] + 1
    print(temp)
print(temp)

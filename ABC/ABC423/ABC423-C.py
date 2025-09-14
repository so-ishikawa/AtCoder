#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, R = map(int, input().split())
L_list = list(map(int, input().split()))

for i in range(len(L_list)-1, R-1, -1):
    if L_list[i] == 0:
        break
    L_list.pop()
count = 0

while len(L_list)>0:
    if R == count:
        break
    if L_list[0] == 0:
        break
    L_list.pop(0)
    count +=1

# print(L_list)
print(L_list.count(1) + len(L_list))

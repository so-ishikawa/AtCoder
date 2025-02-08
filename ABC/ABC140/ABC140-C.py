#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
B_list = list(map(int, input().split()))

A_list = []

if N == 2:
    print(B_list[0]*2)
    exit()
if N == 3:
    print(sum(B_list)+min(B_list))
    exit()

A_list.append(B_list[0])
for i in range(len(B_list)-1):
    A_list.append(min(B_list[i], B_list[i+1]))
A_list.append(B_list[-1])
# print(A_list)
print(sum(A_list))

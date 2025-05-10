#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
A_list = list(map(int, input().split()))

temp = 0
for i_num in range(len(A_list)):
    i = A_list[i_num]
    for j_num in range(len(A_list)):
        j = A_list[j_num]
        # print(i*j)
        if not (i_num < j_num):
            continue

        temp += i*j

print(temp)

#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
import math

N = int(input())
A_list = list(map(int, input().split()))

temp = []
min_ = min(A_list)

for i in range(1, int(math.sqrt(min_))+1):
    if min_ % i == 0:
        temp.append(i)
        temp.append(min_//i)

temp.sort(reverse=True)

for i in temp:
    flag = True
    for j in A_list:
        if j % i != 0:
            flag = False
            break
    if flag:
        print(i)
        exit()


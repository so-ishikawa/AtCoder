#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
import math

N = int(input())
A_list = list(map(int, input().split()))

dic = dict()
dic[1] = 0
dic[2] = 0
dic[3] = 0

for i in A_list:
    dic[i] = dic[i] + 1

temp = 0
for i in [1,2,3]:
    if dic[i] <= 1:
        continue
    temp += (dic[i] * (dic[i]-1)) // 2
print(temp)

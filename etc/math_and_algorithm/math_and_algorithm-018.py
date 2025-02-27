#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
import math

N = int(input())
A_list = list(map(int, input().split()))

dic = dict()
for i in A_list:
    if i in dic:
        dic[i] = dic[i] + 1
        continue
    dic[i] = 1

temp = 0
if 100 in dic and 400 in dic:
    temp += (dic[100]*dic[400])
if 200 in dic and 300 in dic:
    temp += (dic[200]*dic[300])
print(temp)

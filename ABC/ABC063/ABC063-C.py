#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
import itertools

N = int(input())
s_list = []
for i in range(N):
    s_list.append(int(input()))

temp = [x for x in s_list if x % 10 != 0]

if len(temp) == 0:
    print(0)
    exit()

if sum(s_list) % 10 != 0:
    print(sum(s_list))
    exit()

temp = [sum(s_list)-x for x in temp]

print(max(temp))

#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
a_list = list(map(int, input().split()))
temp = []
for i in range(len(a_list)):
    temp.append((i+1, a_list[i]))

temp.sort(key=lambda x: -x[1])

for i in temp:
    print(i[0])

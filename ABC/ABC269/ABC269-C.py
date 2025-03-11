#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())


keta_list = []
while N:
    keta_list.insert(0, N&1)
    N = N >> 1

count = keta_list.count(1)

for i in range((2**count)):
    temp = []
    for j_ in range(len(keta_list)-1, -1, -1):
        j = keta_list[j_]
        if j == 0:
            temp.insert(0, "0")
            continue
        temp.insert(0, str(i&1))
        i = i >> 1

    if len(temp) == 0:
        print(0)
        continue
    print(int("".join(temp),2))

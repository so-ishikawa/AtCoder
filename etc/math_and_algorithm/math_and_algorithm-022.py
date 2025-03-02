#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
from collections import Counter

N = int(input())
A_list = list(map(int, input().split()))
A_list.sort()

temp = Counter(A_list)

A_list = list(set(A_list))
A_list.sort()

count = 0
for i in range(len(A_list)):
    if A_list[i] > 50000:
        break
    # if temp[100000 - A_list[i]] == 0:
    #     continue

    # if A_list[i] == 50000:
    #    if temp[A_list[i]] == 1:
    #        break
    if A_list[i] == 50000:
        count += (temp[A_list[i]]*(temp[A_list[i]]-1))//2
        break

    count += (temp[A_list[i]]*temp[100000-A_list[i]])

print(int(count))

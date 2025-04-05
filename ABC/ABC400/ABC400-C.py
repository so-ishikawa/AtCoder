#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
import bisect

N = int(input())

if N == 2:
    print(1)
    exit()

list2 = []
a = 1
while N > 2**a:
    list2.append(2**a)
    a += 1

listb = []
b = 1
while N > b**2:
    listb.append(b**2)
    b += 1
count_set = set()
# print(listb, list2)
index = len(list2)
for i in listb:
    if i == 0:
        # count_set.add(0)
        continue
    #if not (N / i).is_integer():
    #     continue
    index = bisect.bisect(list2, N/i, hi=index)
    for j in range(index):
        count_set.add(list2[j] * i)
        # print(list2[j], i, " hello!")
print(len(count_set))
# print(count_set)


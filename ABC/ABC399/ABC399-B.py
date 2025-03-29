#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
P_list = list(map(int, input().split()))

temp = P_list.copy()
temp = list(set(temp))
temp.sort(reverse=True)

dic = dict()
rank = 1
for i in temp:
    dic[i] = rank
    rank += P_list.count(i)
for i in P_list:
    print(dic[i])


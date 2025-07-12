#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
import itertools

N, M = map(int, input().split())
X_list = list(map(int, input().split()))

X_list = list(set(X_list))
X_list.sort()

if M == 1:
    print(max(X_list)-min(X_list))
    exit()

if len(X_list) <= M:
    print(0)
    exit()

bet = len(X_list)-1
min_cost = 99999999999999999999999999999999
for i_ in itertools.combinations(range(bet), M-1):
    i = list(i_)
    # print("------", i, "-------")
    temp = []
    temp.append(X_list[0: i[0]+1])
    for j in range(len(i)):
        if j == len(i)-1:
            temp.append(X_list[i[j]+1:])
            continue
        temp.append(X_list[i[j]+1:i[j+1]+1])
    cost = 0    
    for j in temp:
        if len(j) == 1:
            continue
        cost += (max(j)-min(j))
    min_cost = min(min_cost, cost)
print(min_cost)

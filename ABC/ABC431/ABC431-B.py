#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

X = int(input())
N = int(input())
W_list = list(map(int, input().split()))
Q = int(input())
P_list = []
for i in range(Q):
    P_list.append(int(input()))

attached = set()

current = X

for p in P_list:
    if p in attached:
        current -= W_list[p-1]
        attached.remove(p)
        print(current)
        continue

    current += W_list[p-1]
    attached.add(p)
    print(current)

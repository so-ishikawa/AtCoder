#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

N, M, Q = map(int, input().split())
dic = dict()
for i in range(1, N+1):
    dic[i] = set()

capable_set = set()

for _ in range(Q):
    query = list(map(int, input().split()))
    num = query[0]
    X = query[1]
    if len(query) == 3:
        Y = query[2]

    if num == 1:
        dic[X].add(Y)
        continue
    if num == 2:
        capable_set.add(X)
        continue
    else:
        # num == 3
        if Y in dic[X] or X in capable_set:
            print("Yes")
        else:
            print("No")
        

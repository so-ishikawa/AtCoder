#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, M = map(int, input().split())

dic = dict()

for _ in range(M):
    A, B = map(int, input().split())
    if A in dic:
        dic[A].append(B)
    else:
        dic[A] = [B]
    if B in dic:
        dic[B].append(A)
    else:
        dic[B] = [A]

if len(dic.keys()) != N:
    print("No")
    exit()

for k in dic.keys():
    if len(dic[k]) != 2:
        print("No")
        exit()

current = 1
passed_set = set()
for i in range(N):
    if len(passed_set) == 0:
        passed_set.add(current)
        current = max(dic[current])
        continue
    passed_set.add(current)
    temp = [x for x in dic[current] if x not in passed_set]

    if len(temp) == 0:
        if i == N-1:
            print("Yes")
        else:
            print("No")
        exit()

    current = temp[0]

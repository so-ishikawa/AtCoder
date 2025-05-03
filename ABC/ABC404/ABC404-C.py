#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, M = map(int, input().split())

dic = dict()

temp = set()
for i in range(M):
    A, B = map(int, input().split())
    temp.add((min(A, B), max(A, B)))
    if min(A, B) == 1 and max(A, B) == N:
        dic[N] = 1
        continue
    dic[min(A, B)] = max(A, B)
    
if len(temp) != N:
    print("No")
    exit()

next = 1
passed_set = set()
for _ in range(N):
    if next in passed_set and next != 1:
        print("No")
        exit()

    next = dict[next]
    passed_set.add(next)
if next == 1:
    print("Yes")
    exit()
print("No")

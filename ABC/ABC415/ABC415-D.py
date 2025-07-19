#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

N, M = map(int, input().split())
A_list = []
V_list = []
count = 0
for i in range(M):
    A, B = map(int, input().split())
    V = A - B
    V_list.append((V, i))
    A_list.append(A)
    
V_list.sort(key=lambda x: x[0])
current = N
flag = False
for v in V_list:
    diff = v[0]
    index = v[1]
    while True:
        if current < diff:
            flag = True
            break
        if A_list[index] > current:
            break
        current = current - diff
        count += 1
    if flag:
        break
print(count)

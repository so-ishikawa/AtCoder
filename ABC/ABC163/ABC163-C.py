#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
A_list = list(map(int, input().split()))

dic = dict()
for i in range(1, N+1):
    dic[i] = []

for i in range(len(A_list)):
    dic[A_list[i]].append(i+1)

for i in range(1, N+1):
    print(len(dic[i]))

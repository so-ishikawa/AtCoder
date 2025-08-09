#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, M = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_dic = dict()
B_dic = dict()

for a in A_list:
    if a in A_dic:
        A_dic[a] = A_dic[a] + 1
        continue
    A_dic[a] = 1

for b in B_list:
    if b in B_dic:
        B_dic[b] = B_dic[b] + 1
        continue
    B_dic[b] = 1

A_set = set(A_list)
B_set = set(B_list)

A_header = list(A_set)
A_header.sort()
B_header = list(B_set)
B_header.sort()

for h in A_header:
    if h not in B_dic:
        for i in range(A_dic[h]):
            print(h, end=" ")
        continue
    if A_dic[h] <= B_dic[h]:
        continue
    for i in range(A_dic[h]-B_dic[h]):
        print(h, end=" ")


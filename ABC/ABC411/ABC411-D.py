#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

N, Q = map(int, input().split())

word_dic = dict()
count = 0
query_list = []

pc_dic = dict()
for i in range(N+1):
    pc_dic[i] = []

for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 2:
        s = q[2]
        word_dic[count] = s
        count += 1
    query_list.append(q)
    
for q in query_list:
    if q[0] == 1:
        p = q[1]
        
        continue
    if q[0] == 2:
        p = q[1]
        s = q[2]
        continue
    if q[0] == 3:
        p = q[1]
        continue
    

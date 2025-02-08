#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
P_list = list(map(int, input().split()))
Q_list = list(map(int, input().split()))

P_list.insert(0, "dummy")
Q_list.insert(0, "dummy")

dic = dict()

for q_index in range(1, N+1):
    i = Q_list[q_index] 
    no = P_list[q_index]
    temp = Q_list[no]
    dic[i] = temp

for i in range(1, N+1):
    print(dic[i], end=" ")

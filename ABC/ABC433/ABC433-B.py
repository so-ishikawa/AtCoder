#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
A_list = list(map(int, input().split()))

pre = []
for i in range(N):
    pre.append((A_list[i], i))

pre.sort(key=lambda x: x[0])
pre_aft_dic = dict()
aft_pre_dic = dict()

for i in range(N):
    pre_aft_dic[pre[i][1]] = i
    aft_pre_dic[i] = pre[i][1]

# print(pre_aft_dic, aft_pre_dic)
    
for i in range(N):
    if i == 0:
        print(-1)
        continue
    target_aft_index = pre_aft_dic[i]
    for j in range(i-1, -1, -1):
        aft_index = pre_aft_dic[j]
        if target_aft_index < aft_index:
            print(j+1)
            break
        if j == 0:
            print(-1)

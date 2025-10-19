#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

N, K = map(int, input().split())
S = input()
dic = dict()
for i in range(1, N-K+1+1):
    # for j in range(i-1, i+K-1):
    temp = S[i-1:i+K-1-1+1]
    if temp in dic:
        dic[temp] = dic[temp]+1
    else:
        dic[temp] = 1
max_count = max(dic.values())
temp = []
for k, v in dic.items():
    if max_count != v:
        continue
    temp.append(k)
temp.sort()
print(max_count)
for i in temp:
    print(i, end=" ")

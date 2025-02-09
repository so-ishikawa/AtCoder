#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, K = map(int, input().split())
c_list = list(map(int, input().split()))

dic = dict()
for i in range(K):
    dic[c_list[i]] = dic.get(c_list[i], 0) + 1
best_score = len(dic)

for i in range(K, N):
    dic[c_list[i]] = dic.get(c_list[i], 0) + 1
    dic[c_list[i-K]] -= 1
    if dic[c_list[i-K]] == 0:
        dic.pop(c_list[i-K])
    best_score = max(best_score, len(dic))
print(best_score)

#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, M = map(int, input().split())
S_list = []
for i in range(N):
    S = input()
    S_list.append(S)

score = [0]*N

for i in range(M):
    count_0 = 0
    for j in range(N):
        if S_list[j][i] == "0":
            count_0 += 1
    min_value = "0" if count_0*2 < N else "1"
    for j in range(N):
        if S_list[j][i] == min_value:
            score[j] = score[j] + 1

max_value = max(score)
for i in range(N):
    if max_value == score[i]:
        print(i+1, end=" ")







"""
result = [0]*N
for i in range(N):
    S = list(input())
    count_0 = S.count("0")
    count_1 = S.count("1")
    # print(count_0, count_1)
    # target = min(count_0, count_1)
    target = "0" if count_0 < count_1 else "1"
    # print(target)
    for index in range(N):
        if target == S[index]:
            result[index] = result[index]+1
print(result)
max_value = max(result)
for i in range(len(result)):
    if result[i] == max_value:
        print(i+1, end=" ")
"""

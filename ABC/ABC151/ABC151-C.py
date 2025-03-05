#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, M = map(int, input().split())

ACed_list = [False]*(N+1)
WA_count_list = [0]*(N+1)

WA_count = 0
for i in range(M):
    p, S = map(str, input().split())
    p = int(p)

    if S == "AC":
        if ACed_list[p] is True:
            continue
        ACed_list[p] = True
        WA_count += WA_count_list[p]

        continue
    if ACed_list[p]:
        continue
    WA_count_list[p] += 1

print(ACed_list.count(True), WA_count)

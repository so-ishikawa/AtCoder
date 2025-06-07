#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
A_list = list(map(int, input().split()))
A_list.sort()

import bisect
temp = 0
for i in range(N+1):
    index = bisect.bisect_left(A_list, i)
    if i <= N - index:
        # print("debug:", i)
        temp = i
print(temp)

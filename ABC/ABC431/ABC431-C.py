#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, M, K = map(int, input().split())
H_list = list(map(int,input().split()))
B_list = list(map(int, input().split()))

H_list.sort()
B_list.sort()

import bisect

robo_count = 0
used = set()

finish_flag = False
next_free = 0

for h in H_list:
    # while True:
    index = bisect.bisect_left(B_list, h, lo=next_free)
    if index == len(B_list):
        finish_flag = True
        break
    while index != len(B_list):
        if index not in used:
            used.add(index)
            robo_count += 1
            next_free = index + 1
            break
        index = index + 1
        
    if finish_flag:
        break
print("Yes" if robo_count>=K else "No")

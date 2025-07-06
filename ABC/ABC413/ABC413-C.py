#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
from collections import deque

Q = int(input())
group_1_deque = deque()
group_2_list = []
for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        c = q[1]
        x = q[2]
        group_1_deque.append((c, x))
        continue
    # q[0] = 2 
    k = q[1]
    group_2_list.append(k)

carry_over = 0
for _k in group_2_list:
    k = _k
    while True:
        temp = group_1_deque.popleft()
        c = temp[0]
        x = temp[1]
        if k == c:
            print(c*x+carry_over)
            carry_over = 0
            break
        if k > c:
            k = k - c
            carry_over = carry_over + c*x
            continue
        else:
            # k < c:
            print(k*x + carry_over)
            carry_over = 0
            group_1_deque.appendleft((c-k, x))
            break
            

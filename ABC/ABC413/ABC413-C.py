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
    k = q[1]
    group_2_list.append(k)


remain = None
carry_over = 0
for _k in group_2_list:
    k = _k
    while True:
        if remain is not None:
            c = remain[0]
            x = remain[1]
            if c == k:
                print(c*x)
                remain = None
                break
            if c > k:
                print(k*x)
                remain = ((c-k), x)
                break
            if c < k:
                k = k - c
                remain = None
                carry_over = c*x
        
        temp = group_1_deque.popleft()
        c = temp[0]
        x = temp[1]
        if c == k:
            print(c*x + carry_over)
            carry_over = 0
            break
        if c > k:
            print(k*x + carry_over)
            remain = ((c-k),x)
            carry_over = 0
            break
        else:
            # c < k
            k = k - c
            carry_over += c*x
            # remain = None


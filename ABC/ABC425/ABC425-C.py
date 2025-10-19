#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, Q = map(int, input().split())
A_list = list(map(int, input().split()))

head = 0
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        c = q[1]
        head = (head + c) % N
        continue
    else:
        # q[0] == 2
        l = q[1] - 1
        r = q[2] - 1

        l = (l + head) % N
        r = (r + head) % N

        if l > r:
            # 0-r + l -  N-1
            temp = 0
            for i in range(r+1):
                temp += A_list[i]
            for i in range(l, N):
                temp += A_list[i]
        else:
            temp = 0
            for i in range(l, r+1):
                temp += A_list[i]
        print(temp)


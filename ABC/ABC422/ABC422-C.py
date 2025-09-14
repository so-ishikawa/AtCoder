#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
T = int(input())
for _ in range(T):
    na, nb, nc = map(int, input().split())
    # print(min(min(na, nc), abs(na-nc)+nb))
    count = min(na, nc)
    diff = abs(na - nc)

    for count_ in range(count, -1, -1):
        # print(count_)

        if na - count_ + nb + nc - count_ >= count_:
            print(count_)
            break


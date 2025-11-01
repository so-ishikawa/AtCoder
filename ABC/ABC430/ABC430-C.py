#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, A, B = map(int, input().split())
S = input()

set_ = set()
for l in range(N):
    # print(l)
    b_count = 0
    a_count = 0
    for r in range(l, N):
        # print(r,"!")
        if S[r] == "b":
            b_count += 1
            if b_count >= B:
                break
            if a_count >= A:
                set_.add((l, r))
                continue
        else:
            # "a"
            a_count += 1
            if a_count >= A:
                set_.add((l, r))
                continue
print(len(set_))
                

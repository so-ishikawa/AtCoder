#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
next_dic = dict()
w_dic = dict()
# passed_set = set({1})

N, M = map(int, input().split())
for i in range(M):
    A, B, W = map(int, input().split())
    if A in next_dic:
        next_dic[A].append(B)
    else:
        next_dic[A] = [B]
    w_dic[(A, B)] = W


min_w = 99999999999999999999999999999999

def f(current, _passed_set, _total):
    global min_w
    if current == N:
        if min_w > _total:
            min_w = _total

    if current not in next_dic:
        return

    for i in next_dic[current]:
        if (current, i) in _passed_set:
            continue
        temp_set = _passed_set.copy()
        temp_set.add((current, i))
        _new_total = _total ^ w_dic[(current, i)]
        f(i, temp_set, _new_total)

passed_set = set()
f(1, passed_set.copy(), 0)

if min_w == 99999999999999999999999999999999:
    print(-1)
    exit()
print(min_w)

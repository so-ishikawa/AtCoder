#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, M = map(int, input().split())
uv_dic = dict()
w_dic = dict()

for i in range(M):
    u, v, w = map(int, input().split())
    uv_dic.setdefault(u, []).append(v)
    uv_dic.setdefault(v, []).append(u)
    w_dic.setdefault((min(u,v), max(u,v)), []).append(w)
# print(w_dic)
min_xor_value = 9999999999999999999999999999999
def f(position, memo, current_xor):
    global min_xor_value
    if position == N:
        if current_xor < min_xor_value:
            min_xor_value = current_xor
        return
    next_list = uv_dic[position]
    next_list = [x for x in next_list if x not in memo]
    

    for i in next_list:
        _memo = memo.copy()
        _memo.add(i)
        w = w_dic[(min(i, position), max(i, position))][0]
        f(i, _memo, current_xor^w)

f(1, set({1}), 0)
print(min_xor_value)

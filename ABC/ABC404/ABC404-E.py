#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
import sys
sys.setrecursionlimit(20000000)

N = int(input())
C_list = list(map(int, input().split()))
A_list = list(map(int, input().split()))

C_list.insert(0, "dummy")
A_list.insert(0, "dummy")

exist_list = []
for i in range(len(A_list)):
    if i == 0:
        continue
    if A_list[i] != 0:
        exist_list.append(i)

min_count = 99999999999999999999999999999
def f(_current, _exist_list, _count):
    global min_count
    global C_list
    global A_list
    # print(_current)
    if _count > N:
        return
    
    if _current == 0 and len(_exist_list) == 0:
        min_count = min(min_count, _count)
        return

    if _current == 0:
        f(max(_exist_list), _exist_list.copy(), _count)
        return

    if _current in _exist_list:
        _exist_list.remove(_current)

    for i in range(max(0, _current-C_list[_current]), N):
        f(i, _exist_list.copy(), _count+1)

current = exist_list[-1]
f(current, exist_list.copy(), 0)

print(min_count)

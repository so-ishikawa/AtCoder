#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
import math

N = int(input())
A_list = list(map(int, input().split()))

dic = dict()

for i in A_list:
    _dic = dict()
    n = i
    for j in range(2, int(math.sqrt(i))+1):
        while n % j == 0:
            n /= j
            if j in _dic:
                _dic[j] = _dic[j] + 1
                continue
            _dic[j] = 1

    n = int(n)
    if n >= 2:
        if n in _dic:
            _dic[n] = _dic[n] + 1
        else:
            _dic[n] = 1
    
    for k in _dic.keys():
        if k not in dic:
            dic[k] = _dic[k]
            continue
        if dic[k] < _dic[k]:
            dic[k] = _dic[k]

temp = 1
for k in dic:
    temp *= k**dic[k]
print(temp)

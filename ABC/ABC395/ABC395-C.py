#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
import collections

N = int(input())
A_list = list(map(int, input().split()))

set_ = set(A_list)
if len(set_) == N:
    print(-1)
    exit()

double_set = set([k for k, v in collections.Counter(A_list).items() if v > 1])
check_dic = dict()
min_length = 999999999999999999999999999999999

for i in range(len(A_list)):
    if A_list[i] not in double_set:
        continue
    if A_list[i] not in check_dic:
        check_dic[A_list[i]] = i
        continue
    temp = i - check_dic[A_list[i]] + 1
    if min_length > temp:
        min_length = temp
    check_dic[A_list[i]] = i
print(min_length)

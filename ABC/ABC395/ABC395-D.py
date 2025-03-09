#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, Q = map(int, input().split())

hato_label = dict()

label_num = dict()
num_label = dict()

for i in range(1, N+1):
    hato_label[i] = i
    label_num[i] = i
    num_label[i] = i

for _ in range(Q):
    op = list(map(int, input().split()))
    if op[0] == 1:
        a = op[1]
        b = op[2]
        label = num_label[b]
        hato_label[a] = label
        continue
    if op[0] == 2:
        a = op[1]
        b = op[2]

        label_a = num_label[a]
        label_b = num_label[b]
        num_label[a] = label_b
        num_label[b] = label_a

        label_num[label_a] = b
        label_num[label_b] = a
        continue
    # op[0] == 3:
    a = op[1]
    label = hato_label[a]
    num = label_num[label]
    print(num)

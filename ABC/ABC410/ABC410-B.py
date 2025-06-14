#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, Q = map(int, input().split())
X_list = list(map(int, input().split()))

ball_list = list()
box_list = [0]*N
box_list.insert(0, "dummy")

for i in range(len(X_list)):
    X = X_list[i]
    if X >= 1:
        box_list[X] = box_list[X] + 1
        ball_list.append(X)
        continue

    min_index = 999999999999999999999999
    min_value = 999999999999999999999999
    for j in range(1, N+1):
        if box_list[j] < min_value:
            min_index = j
            min_value = box_list[j]
    box_list[min_index] = box_list[min_index] + 1
    ball_list.append(min_index)

for i in ball_list:
    print(i, end=" ")

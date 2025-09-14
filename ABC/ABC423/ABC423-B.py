#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
L_list = list(map(int, input().split()))

left = 1
right = 1

last_room_left = 0
last_room_right = N

for i in range(len(L_list)):
    if L_list[i] == 1:
        break
    left += 1
    last_room_left = i+1

for i in range(len(L_list)-1, -1, -1):
    if L_list[i] == 1:
        break
    right += 1
    last_room_left = i

print(max(N+1-left-right, 0))

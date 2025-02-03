#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

N, M, H, K = map(int, input().split())
S = input()

item_set = set()

for i in range(M):
    x, y = map(int, input().split())
    item_set.add((x, y))

current_x = 0
current_y = 0

move_count = 0

for s in S:
    H -= 1
    move_count += 1
    if s == "R":
        current_x += 1
    elif s == "L":
        current_x -= 1
    elif s == "U":
        current_y += 1
    elif s == "D":
        current_y -= 1

    if H < 0:
        """
        if move_count == N:
            print("Yes")
            exit()
        else:
        """
        print("No")
        exit()

    if (current_x, current_y) in item_set:
        if H < K:
            H = K
            item_set.discard((current_x, current_y))
print("Yes")
    
    

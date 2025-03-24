#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, R, C = map(int, input().split())
S = input()

smoke_set = set()
smoke_set.add((0, 0))

origin_x = 0
origin_y = 0

takahashi_x = R
takahashi_y = C

result = ""

for s in S:
    if s == "N":
        origin_x += 1
        takahashi_x += 1
    if s == "W":
        origin_y += 1
        takahashi_y += 1
    if s == "S":
        origin_x -= 1
        takahashi_x -= 1
    if s == "E":
        origin_y -= 1
        takahashi_y -= 1

    smoke_set.add((origin_x, origin_y))
    # print(smoke_set, (takahashi_x, takahashi_y))
    if (takahashi_x, takahashi_y) in smoke_set:
        result += "1"
        continue
    result += "0"
print(result)

#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
H, W = map(int, input().split())
S_list = []
for i in range(H):
    S_list.append(input())

black_set = set()

for h in range(H):
    for w in range(W):
        if S_list[h][w] == "#":
            black_set.add((h, w))

do_not_think_set = set()

positive_set = set()
count = 0
while True:
    for b in black_set:
        h, w = b
        if h - 1 >= 0:
            if (h-1, w) in do_not_think_set:
                pass
            elif (h-1, w) in positive_set:
                do_not_think_set.add((h-1, w))
                positive_set.remove((h-1, w))
            else:
                positive_set.add((h-1, w))
        if h + 1 < H:
            if (h+1, w) in do_not_think_set:
                pass
            elif (h+1, w) in positive_set:
                do_not_think_set.add((h+1, w))
                positive_set.remove((h+1, w))
            else:
                positive_set.add((h+1, w))
        if w - 1 >= 0:
            if (h, w-1) in do_not_think_set:
                pass
            elif (h, w-1) in positive_set:
                do_not_think_set.add((h, w-1))
                positive_set.remove((h, w-1))
            else:
                positive_set.add((h, w-1))
        if w + 1 < W:
            if (h, w+1) in do_not_think_set:
                pass
            elif (h, w+1) in positive_set:
                do_not_think_set.add((h, w+1))
                positive_set.remove((h, w+1))
            else:
                positive_set.add((h, w+1))

    black_set = black_set.union(positive_set)
    positive_set.clear()

    if len(black_set) == count:
        break
    count = len(black_set)
print(count)

#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
T = int(input())

for _ in range(T):
    H, W = map(int, input().split())
    ban = []
    for _ in range(H):
        ban.append(input())

    hyo = []
    for h in range(H):
        temp = []
        for w in range(W):
            temp.append([])
        hyo.append(temp)

    for h in range(H-1):
        for w in range(W-1):
            if not (ban[h][w] == "#" and ban[h][w+1] == "#" and ban[h+1][w] == "#" and ban[h+1][w+1] == "#"):
                continue
            hyo[h][w].append("lu")
            hyo[h][w+1].append("ru")
            hyo[h+1][w].append("ld")
            hyo[h+1][w+1].append("rd")

    count = 0
    # print(hyo)
    while True:
        # print(count)
        max_count = 0
        current_max_h = -1
        current_max_w = -1
        for h in range(H):
            for w in range(W):
                if len(hyo[h][w]) > max_count:
                    current_max_h = h
                    current_max_w = w
                    max_count = len(hyo[h][w])
        
        if max_count == 0:
            break
        # print(hyo)
        ch = current_max_h
        cw = current_max_w
        # print(hyo[ch][cw])
        aa = hyo[ch][cw].copy()
        for t in aa:
            # print(t)
            if t == "lu":
                hyo[ch][cw].remove("lu")
                hyo[ch][cw+1].remove("ru")
                hyo[ch+1][cw].remove("ld")
                hyo[ch+1][cw+1].remove("rd")
            if t == "ru":
                hyo[ch][cw].remove("ru")
                hyo[ch][cw-1].remove("lu")
                hyo[ch+1][cw].remove("rd")
                hyo[ch+1][cw-1].remove("ld")
            if t == "ld":
                hyo[ch][cw].remove("ld")
                hyo[ch-1][cw].remove("lu")
                hyo[ch-1][cw+1].remove("ru")
                hyo[ch][cw+1].remove("rd")
            if t == "rd":
                hyo[ch][cw].remove("rd")
                hyo[ch-1][cw-1].remove("lu")
                hyo[ch][cw-1].remove("ld")
                hyo[ch-1][cw].remove("ru")
        count = count + 1
    print(count)

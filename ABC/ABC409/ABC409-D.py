#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
T = int(input())
for _ in range(T):
    length = int(input())
    target = input()

    start = None
    for i in range(length-1):
        if target[i] > target[i+1]:
            start = i
            break

    if start is None:
        print(target)
        continue

    end = None
    start_word = target[start]
    for i in range(start+1, length):
        if start_word < target[i]:
            end = i-1
            break
    if end is None:
        end = length - 1

    target_list = list(target)
    pre = target_list[0:start]
    cent = target_list[start:end+1]
    aft = target_list[end+1:length]
    #print(pre, cent, aft, "!!")
    move_ = cent.pop(0)
    cent.append(move_)

    temp = (pre + cent + aft)
    print("".join(temp))

#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
import bisect

T = int(input())
for i in range(T):
    N = int(input())
    S_list = list(map(int, input().split()))

    left = S_list.pop(0)
    right = S_list.pop()
    S_list.sort()

    if len(S_list) == 0:
        if left*2 >= right:
            print(2)
            continue
        else:
            print(-1)
            continue

    count = 1
    index = 0
    success = False
    while True:
        if count == 1:
            target = left
        else:
            target = S_list[index]
        next_index = bisect.bisect(S_list, target*2)
        
        if next_index == index + 1 and count != 1:
            break
        else:
            if count == 1 and next_index == 0:
                break
        if next_index == len(S_list):
            if target*2 >= right:
                count += 1
                success = True
                break
            count += 1
            if S_list[-1]*2 >= right:
                count += 1
                success = True
                break
            break

        count += 1
        index = next_index -1


    if success:
        print(count)
        continue
    else:
        print(-1)
        continue

#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

import itertools
import math

dic = dict({0:[[1,2],[3,6],[4,8]],
            1:[[0,2],[4,7]],
            2:[[0,1],[5,8],[4,6]],
            3:[[0,6],[4,5]],
            4:[[1,7],[3,5],[0,8],[2,6]],
            5:[[2,8],[3,4]],
            6:[[0,3],[2,4],[7,8]],
            7:[[1,4],[6,8]],
            8:[[2,5],[0,4],[6,7]]})

box = []
box += list(map(int, input().split()))
box += list(map(int, input().split()))
box += list(map(int, input().split()))



count = 0
flag_list = [False]*9
for v in itertools.permutations(range(8+1), 9):
    # print(v)
    for i in range(9):
        flag_list[i] = False

    flag = False
    for i in v:
        for b in dic[i]:
            if box[b[0]] == box[b[1]] and flag_list[b[0]] and flag_list[b[1]]:
                flag = True
                break
        if flag:
            break
        flag_list[i] = True
    if flag:
        continue
        
    count += 1

# print(count, len(itertools.permutations(list(range(8+1)),9))
print(count/len(list(itertools.permutations(range(8+1), 9))))
# print(len(a))

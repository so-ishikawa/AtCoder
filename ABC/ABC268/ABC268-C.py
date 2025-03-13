#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
p_list = list(map(int, input().split()))

move_score_list = [0]*N
dish_position_dic = dict()
for i in range(len(p_list)):
    dish_position_dic[p_list[i]] = i

for i in range(N):
    if i < dish_position_dic[i]:
        move_diff = i + N - dish_position_dic[i]
    else:
        move_diff = i - dish_position_dic[i]

    move_score_list[move_diff] = move_score_list[move_diff] + 1
    if move_diff == 0:
        move_score_list[N-1] = move_score_list[N-1]+1
        move_score_list[1] = move_score_list[1]+1
    elif move_diff == N-1:
        move_score_list[0] = move_score_list[0] + 1
        move_score_list[N-2] = move_score_list[N-2] + 1
    else:
        move_score_list[move_diff-1] = move_score_list[move_diff-1] + 1
        move_score_list[move_diff+1] = move_score_list[move_diff+1] + 1

temp = (-1, 0)
for i in range(len(move_score_list)):
    if move_score_list[i] > temp[1]:
        temp = (i, move_score_list[i])
print(temp[1])

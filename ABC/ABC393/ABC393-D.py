#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
import bisect

N = int(input())
S = input()

position_index_dic = dict()
index_position_dic = dict()

is_position_set = set() 

index = 0
for i in range(len(S)):
    if S[i] == "0":
        continue
    # "1"case
    position_index_dic[i] = index
    index_position_dic[index] = i
    is_position_set.add(i)
    index += 1

position_list = list(is_position_set)
position_list.sort()

count_one_num = S.count("1")

min_cost = 999999999999999999999999999999999
for i_ in range(count_one_num//2, min(count_one_num//2+2, count_one_num)):
    i = index_position_dic[i_]
    if i in is_position_set:
        center_index = position_index_dic[i]
        cost = 0
        # right
        next_position = i
        for j in range(center_index+1, count_one_num):
            position = index_position_dic[j]
            cost += abs(position - (next_position+1))
            next_position += 1

        next_position = i
        for j in range(center_index-1, -1, -1):
            position = index_position_dic[j]
            cost += abs(position - (next_position-1))
            next_position -= 1 

        min_cost = min(min_cost, cost)
        continue
    else:
        _index = bisect.bisect(position_list, i)
        cost = 0
        if _index == 0:
            center_index = 0
            # right
            cost += abs(i-index_position_dic[center_index])
            next_position = i
            for j in range(center_index+1, count_one_num):
                position = index_position_dic[j]
                cost += abs(position - (next_position+1))
                next_position += 1 
            # print(i, cost)
            min_cost = min(min_cost, cost)
            continue

        elif _index == count_one_num:
            center_index = count_one_num-1
            # left
            cost += abs(i-index_position_dic[center_index])
            next_position = i
            for j in range(center_index-1, -1, -1):
                position = index_position_dic[j]
                cost += abs(position - (next_position-1))
                next_position -= 1 
            # print(i, cost)
            min_cost = min(min_cost, cost)
            continue

        else:
            left_index = _index-1
            right_index = _index

            # right
            center_index = right_index
            right_cost = abs(i-index_position_dic[center_index])
            # right_right
            next_position = i
            for j in range(center_index+1, count_one_num):
                position = index_position_dic[j]
                right_cost += abs(position - (next_position+1))
                next_position += 1
            # right_left
            next_position = i
            for j in range(center_index-1, -1, -1):
                position = index_position_dic[j]
                right_cost += abs(position - (next_position-1))
                next_position -= 1

            # left
            center_index = left_index
            left_cost = abs(i-index_position_dic[center_index])
            # left_right
            next_position = i
            for j in range(center_index+1, count_one_num):
                position = index_position_dic[j]
                left_cost += abs(position - (next_position+1))
                next_position += 1 
            # left_left
            next_position = i
            for j in range(center_index-1, -1, -1):
                position = index_position_dic[j]
                left_cost += abs(position - (next_position-1))
                next_position -= 1
            # print(i, right_cost, left_cost)
            min_cost = min(min_cost, right_cost, left_cost)
            continue

print(min_cost)

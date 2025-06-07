#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, L = map(int, input().split())
d_list = list(map(int, input().split()))

length_list = [0]
double_dic = dict()
double_dic[0] = 1
sum_ = 0
for d in d_list:
    sum_ = (sum_ + d) % L
    length_list.append(sum_)
    if sum_ not in double_dic:
        double_dic[sum_] = 1
        continue
    else:
        double_dic[sum_] = double_dic[sum_] + 1

length_list = list(set(length_list))
length_list.sort()
# print(length_list)
exist_set = set(length_list)
# print(double_dic)
count = 0
for d in length_list:
    # if d == 1:
    #     print(d in exist_set, (d+L/3) in exist_set, (d+2*(L/3)) in exist_set)
    if d >= L/3:
        break
    if d in exist_set and (d + L/3) in exist_set and (d + 2*(L/3)) in exist_set:
        
        temp = (double_dic[d] * double_dic[d+L/3] * double_dic[d+2*(L/3)])
        # print(temp)
        count += temp
print(count)

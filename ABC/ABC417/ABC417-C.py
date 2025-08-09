#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

N = int(input())
A_list = list(map(int, input().split()))

me_list = list()
for i in range(1, len(A_list)+1):
    me_list.append(i+A_list[i-1])

you_list = list()
for i in range(1, len(A_list)+1):
    you_list.append(i-A_list[i-1])

t_dic = dict()
t_dic_list = []
for i in range(len(A_list)-1, -1, -1):
    if you_list[i] in t_dic:
        t_dic[you_list[i]] = t_dic[you_list[i]] + 1
    else:
        t_dic[you_list[i]] = 1
    t_dic_list.insert(0, t_dic.copy())

count = 0
for i in range(len(me_list)-1):
    if me_list[i] not in t_dic_list[i]:
        continue
    count = count + t_dic_list[i][me_list[i]]
print(count)
    

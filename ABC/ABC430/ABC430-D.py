#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
X_list = list(map(int, input().split()))
X_list.append(0)

order_positon_dic = dict()

for index in range(len(X_list)):
    order_positon_dic[index] = X_list[index]

X_list.sort()

sorted_position_index = dict()

for index in range(len(X_list)):
    sorted_position_index[X_list[index]] = index

temp = []

for index in range(len(X_list)):
    if index == 0:
        temp.append([abs(X_list[1]-X_list[0])])
        continue
    if index == len(X_list)-1:
        temp.append([abs(X_list[index-1]-X_list[index-2])])
        continue

    temp.append([abs(X_list[index-1]-X_list[index]),abs(X_list[index+1]-X_list[index])])

for i in range(len(order_positon_dic)-1, -1, -1):
    print(order_positon_dic[i])
    

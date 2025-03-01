#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, Q = map(int, input().split())

hato_to_label_dic = dict()
label_to_num_dic = dict()
su_set_list = []

for i in range(1, N+1):
    hato_to_label_dic[i] = i
    label_to_num_dic[i] = i

def get_label_from_num(num):
    keys = [k for k, v in label_to_num_dic.items() if v == num]
    return(keys[0])

for i in range(N+1):
    if i == 0:
        su_set_list.append("dummy")
        continue
    su_set_list.append(set({i}))


for _ in range(Q):
    op = list(map(int, input().split()))
    if op[0] == 1:
        a = op[1]
        b = op[2]
        su_set_list[label_to_num_dic[hato_to_label_dic[a]]].remove(a)
        new_label = get_label_from_num(b)
        su_set_list[label_to_num_dic[new_label]].add(a)
        
        continue

    if op[0] == 2:
        a = op[1]
        b = op[2]
        a_label = hato_to_label_dic[a]
        b_label = hato_to_label_dic[b]
        a_num = label_to_num_dic[a_label]
        b_num = label_to_num_dic[b_label]
        label_to_num_dic[a_label] = b_num
        label_to_num_dic[b_label] = a_num
        continue

    # op[0] == 3:
    a = op[1]
    print(label_to_num_dic[hato_to_label_dic[a]])

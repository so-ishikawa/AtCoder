#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N, Q = map(int, input().split())

su_list = [1]*(N+1)
su_list[0] = "dummy"

bird_dic = dict()
for i in range(N+1):
    bird_dic[i] = i
over_num = 0


for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        P = query[1]
        H = query[2]
        current_su = bird_dic[P]
        # current_num = su_list[current_su]
        su_list[current_su] = su_list[current_su]-1
        if su_list[current_su] == 1:# and su_list[current_su] == 1:
            over_num -= 1
        next_su = H
        su_list[next_su] = su_list[next_su] + 1
        if su_list[next_su] == 2:
            over_num += 1
        bird_dic[P] = H
            
    else:
        #query[0] == 2
        print(over_num)

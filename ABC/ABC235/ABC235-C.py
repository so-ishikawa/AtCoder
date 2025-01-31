#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

N, Q = map(int, input().split())
a_list = list(map(int, input().split()))

big_dic = dict()
for index in range(len(a_list)):
    a = a_list[index]
    if a in big_dic:
        big_dic[a][len(big_dic[a].keys())+1] = index + 1
    else:
        big_dic[a] = dict()
        big_dic[a][1] = index + 1

for i in range(Q):
    x, k = map(int, input().split())
    if x not in big_dic:
        print(-1)
        continue
    if k not in big_dic[x]:
        print(-1)
        continue
    print(big_dic[x][k])


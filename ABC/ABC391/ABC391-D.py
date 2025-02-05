#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

N, W = map(int, input().split())

block_list = [None]*N
block_list.insert(0, "dummy")

index_to_y_dic = dict()

vanish_time_list = [True]*N
vanish_time_list.insert(0, "dummy")


grid = []
for i in range(W):
    grid.append([])

for i in range(N):
    X, Y = map(int, input().split())
    grid[X-1].append((i+1, Y-1)) # index, Y
    index_to_y_dic[i+1] = Y-1

Q = int(input())
    
TA_list = []
for i in range(Q):
    T, A = map(int, input().split())
    TA_list.append((T, A-1))

size_min = 999999999999999
for i in range(W):
    grid[i].sort(key=lambda x: x[1])
    size_min = min(size_min, len(grid[i]))

vanish_group = []
exist_set = set()

for i in range(size_min):
    vanish_group.append(set())

for i in range(W):
    for j in range(len(grid[i])):
        if j >= size_min:
            exist_set.add(grid[i][j][0])
            continue
        vanish_group[j].add(grid[i][j][0])#indexのみ

for i in range(len(vanish_group)):
    max_value = 0
    for j in vanish_group[i]:
        max_value = max(max_value, index_to_y_dic[j])
    for j in vanish_group[i]:
        vanish_time_list[j] = max_value + 1

vanish_time_list.pop(0)

# print(vanish_time_list)
for i in TA_list:
    t, a = i
    # a = a-1
    # print(t, a, vanish_time_list[a])
    if vanish_time_list[a] is True:
        print("Yes")
        continue
    if vanish_time_list[a] > t + 0.5:
        print("Yes")
        continue
    print("No")
    

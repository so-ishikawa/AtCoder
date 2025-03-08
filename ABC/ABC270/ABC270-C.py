#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

N, X, Y = map(int, input().split())
index_list = [0]*(N+1)

min_set = set()

for i in range(1, N):
    U, V = map(int, input().split())
    index_list[max(U,V)] = min(U,V) 

    min_set.add(U)
    min_set.add(V)

root = min(min_set)

if X == Y == root:
    print(root)
    exit()

X_root = [X]
Y_root = [Y]

current = X
while current != root:
    current = index_list[current]
    X_root.append(current)

current = Y
while current != root:
    current = index_list[current]
    Y_root.append(current)

Y_root.pop()
Y_root.reverse()

temp = X_root + Y_root
print(*temp)

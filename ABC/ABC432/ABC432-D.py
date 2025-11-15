#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

N, X, Y = map(int, input().split())

black_set = set()

for x in range(X):
    for y in range(Y):
        black_set.add((x, y))

old_set = black_set.copy()
current_set = set()
# print(old_set)
for _ in range(N):
    C, A, B = map(str, input().split())
    A = int(A)
    B = int(B)

    if C == "X":
        for x, y in old_set:
            if x < A:
                current_set.add((x, y + B))
                continue
            else:
                # x >= A:
                current_set.add((x, y - B))
                continue
    else:
        # C == "Y"
        for x, y in old_set:
            if y < A:
                current_set.add((x + B, y))
                continue
            else:
                current_set.add((x - B, y))
                continue
    old_set = set()
    old_set = current_set.copy()
    current_set = set()
    # print(old_set)

min_x = 999999999999999999999999999
min_y = 999999999999999999999999999
max_x = -99999999999999999999999999
max_y = -99999999999999999999999999

for x, y in old_set:
    if x < min_x:
        min_x = x
    if x > max_x:
        max_x = x
    if y < min_y:
        min_y = y
    if y > max_y:
        max_y = y

# f = UnionFind()

result = []

for x in range(min_x, max_x+1):
    for y in range(min_y, max_y+1):
        if (x, y) not in old_set:
            continue
        if result == []:
            result.append(set({(x, y)}))
            continue
        if (x, y+1) in old_set:
            for i in result:
                if (x, y+1) in i:
                    i.add((x, y+1))
                    break
        if (x+1, y) in old_set:
            for i in result:
                if (x+1, y) in i:
                    i.add((x+1, y))
                    break
print(result)
print(len(result))

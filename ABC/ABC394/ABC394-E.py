#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
N = int(input())
C_list = []
dic = dict()

for i in range(N):
    temp = input()
    C_list.append(temp)
    for j in range(len(temp)):
        if temp[j] == "-":
            continue
        dic.setdefault(i, []).append(j)


def f(i, j):
    temp = [[i, ""]]
    result = []
    
    for _ in range(N):
        for i_ in temp:
            for j_ in dic[i_[0]]:
                char = C_list[i_[0]][j_]
                r = i_[1] + char

                if j_ == j:
                    t = r[-1*(len(r)//2):]
                    if t[::-1] == r[:len(r)//2]:
                        return(len(r))
                result.append([j_, r])
        temp = []
        temp = result
    return(-1)

for i in range(N):
    for j in range(N):
        if i == j:
            print(0, end=" ")
            continue
        if C_list[i][j] != "-":
            print(1, end=" ")
            continue
        print(f(i, j), end= " ")
        continue
    print("")


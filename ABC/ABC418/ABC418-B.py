#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
S = list(input())
if S.count("t") < 3:
    print(0)
    exit()
_size = len(S)
for i in range(_size-1,-1,-1):
    if S[-1] == "t":
        break
    S.pop()
S.reverse()
_size = len(S)
for i in range(_size-1,-1,-1):
    if S[-1] == "t":
        break
    S.pop()
S.reverse()
# print(S,"!!!!")
index_list = []
for i in range(len(S)):
    if S[i] == "t":
        index_list.append(i)
max_value = 0
for start in range(len(index_list)-2):
    # print(start)
    # if start + 2 > (len(index_list) -1):
    #    break
    for end in range(start+2, len(index_list), 1):
        s_start = index_list[start]
        s_end = index_list[end]
        # print(s_start, s_end)
        # print(start, end)
        # print(S[start:end+1])
        x = end - start + 1
        t = len(S[s_start:s_end+1])
        # print(x, t, "!!")
        ans = (x-2)/(abs(t)-2)
        # print(ans,"???")
        max_value = max(ans, max_value)

print(max_value)

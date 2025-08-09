#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-

end_flag = False
def f(current, dic, _pass_set, route, goal):
    global end_flag
    if end_flag:
        return
    if current == goal:
        if route[-1] != goal: 
            route.append(goal)
        for i in route:
            print(i, end = " ")
        print("")
        end_flag = True
        return
            
    if current not in dic:
        return
    temp = dic[current]
    temp.sort()
    for i in temp:
        if i in _pass_set:
            continue
        _copy_pass = _pass_set.copy()
        _copy_route = route.copy()
        _copy_pass.add(i)
        _copy_route.append(i)
        f(i, dic, _copy_pass, _copy_route, goal)



T = int(input())
for _ in range(T):
    end_flag = False
    N, M, X, Y = map(int, input().split())
    dic = dict()
    for _ in range(M):
        U, V = map(int, input().split())
        if U in dic:
            dic[U].append(V)
        else:
            dic[U] = [V]
        if V in dic:
            dic[V].append(U)
        else:
            dic[V] = [U]
    #print(dic)
    temp = dic[X]
    temp.sort()
    for i in temp:
        if end_flag:
            break
        f(i ,dic, set({X}), [X], Y)
            

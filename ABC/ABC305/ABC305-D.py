# -*- coding: utf-8-with-signature -*- 
import bisect

N = int(input())
A_list = list(map(int, input().split()))
Q = int(input())
Q_list = []
for i in range(Q):
    l, r = map(int, input().split())
    Q_list.append((l, r))

start_dic = dict()
start_list = []


for i in range(len(A_list)-1):
    if i == 0:
        continue
    if i % 2 == 1: #start sleep
        start_dic[A_list[i]] = A_list[i+1] - A_list[i]
        start_list.append(A_list[i])
        continue


for i in Q_list:
    input_start_time = i[0]
    input_end_time = i[1]

    start_index = bisect.bisect(A_list, input_start_time) - 1
    end_index = bisect.bisect(A_list, input_end_time) - 1

    # input_start_timeが寝ている時間か起きている時間かで場合分け

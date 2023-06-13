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
    sleep_time_at_start = 0
    next_start_index = 0
    ## 寝ているケース
    if A_list[start_index] in start_dic:
        sleep_time_at_start = A_list[start_index] + start_dic[A_list[start_index]] - input_start_time
        next_start_index = start_index + 2
    else:
        next_start_index = start_index + 1


    ## 寝ているケース
    sleep_time_at_end = 0
    pre_end_index = 0
    if A_list[end_index] in start_dic:
        sleep_time_at_end = input_end_time - A_list[end_index]
        pre_end_index = end_index
    else:
        pre_end_index = end_index - 1

    total = sleep_time_at_start + sleep_time_at_end
    for i in range(next_start_index, pre_end_index, 2):
        total = total + start_dic[A_list[i]]
    print(total)
    

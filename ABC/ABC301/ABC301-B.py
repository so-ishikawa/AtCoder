# A, B = map(int, input().split())
# l = list(map(int, input().split()))
from copy import deepcopy

N = int(input())
A_list = list(map(int, input().split()))

# temp = deepcopy(A_list)
while True:
    for index in range(len(A_list)):
        if index == len(A_list)-1:
            break
        if A_list[index] < A_list[index+1]:
            if A_list[index] == A_list[index+1] - 1:
                continue
            diff = A_list[index+1] - A_list[index]
            diff_list = list(range(A_list[index]+1, A_list[index+1]))
            # print(diff_list,A_list, "??")
            A_list[index+1:index+1] = diff_list
            break
        if A_list[index] > A_list[index+1]:
            if A_list[index] == A_list[index+1] + 1:
                continue
            diff = A_list[index] - A_list[index+1]
            diff_list = list(range(A_list[index]-1, A_list[index+1],-1))
            # print(diff_list,A_list, "!!")
            A_list[index+1:index+1] = diff_list
            break
    # 確認処理
    for index in range(len(A_list)):
        if index == len(A_list)-1:
            #出力
            # print(A_list)
            for i in A_list:
                print(i, end=" ")
            exit()
        # print(A_list[index+1],A_list)
        if A_list[index] == A_list[index+1] - 1:
            continue
        if A_list[index] == A_list[index+1] + 1:
            continue
        break
    # print(A_list)

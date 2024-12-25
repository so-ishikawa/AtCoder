N = int(input())
Q_list = list(map(int, input().split()))
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

min_QA = 999999999999999999999999999
for q, a in zip(Q_list, A_list):
    if a == 0:
        continue
    if min_QA > q//a:
        min_QA = q//a

max_ = 0
for i in range(min_QA+1):
    min_QB = 99999999999999999999999
    temp = Q_list.copy()
    for j in range(N):
        temp[j] -= i*A_list[j]

    
    for q, b in zip(temp, B_list):
        if b == 0:
            continue
        if min_QB > q//b:
            min_QB = q//b

    if max_ < i + min_QB:
        max_ = i + min_QB

print(max_)


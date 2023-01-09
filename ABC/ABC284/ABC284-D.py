# memo
# 2783775885634149388 2
# のようなケースではsqrtの誤差で値がおかしくなる

import math
T = int(input())
test_list = []
for i in range(T):
    n = int(input())
    test_list.append(n)



for i in test_list:
    temp = 0
    p = -1
    q = -1
    for j in range(i):
        if j == 0 or j == 1:
            continue
        if i % j != 0:
            continue
        temp = j
        if i % (temp*temp) == 0:
            p = temp
            q = i // (temp*temp)
            # print(temp, temp*temp, i/(temp*temp))
        else:
            q = temp
            p = int(math.sqrt(i // temp))
        print(p,q)
        break



"""
#str型で受け取るとき
s = input()
#int型で受け取るとき
s = int(input())
# 入力が整数の時
A, B = map(int, input().split())
#list型で取得
l = list(map(int, input().split()))
"""

"""
for i in test_list:
    temp = 0
    p = -1
    q = -1
    for j in range(i):
        if j == 0 or j == 1:
            continue
        if i % j == 0:
            temp = j
            break
    if i % (temp*temp) == 0:
        p = temp
        q = int(i / (temp*temp))
    else:
        q = temp
        p = int(math.sqrt(i / temp))
    print(p,q)
"""




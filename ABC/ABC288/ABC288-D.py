"""
#str型で受け取るとき
s = input()
#int型で受け取るとき
s = int(input())

A, B = map(int, input().split())

l = list(map(int, input().split()))
"""
N, K = map(int, input().split())
a_list = list(map(int, input().split()))
Q = int(input())
l_list = []
r_list = []
for i in range(Q):
    l, r = map(int, input().split())
    l_list.append(l)
    r_list.append(r)

for i in range(Q):
    # ここで各処理を行う
    temp_result = []
    l = l_list[i]
    r = r_list[i]
    target_list = a_list[l-1:r]
    n = r - l + 1
    for j in range(len(Q),0,-1):
        for o in range(K-1):
            if (n - j -1 + o) < 1:
                pass
            

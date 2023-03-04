"""
#str型で受け取るとき
s = input()
#int型で受け取るとき
s = int(input())

A, B = map(int, input().split())

l = list(map(int, input().split()))
"""
N, Q = map(int, input().split())

# event_list = []

yellow_dic = {}
red_dic = {}

for i in range(Q):
    c, x =  map(int, input().split())
    if c == 1:
        if x not in yellow_dic:
            yellow_dic[x] = ""
            continue
        else:
            red_dic[x] = ""
            continue
    elif c == 2:
        red_dic[x] = ""
        continue
    else:
        if x in red_dic:
            print("Yes")
        else:
            print("No")

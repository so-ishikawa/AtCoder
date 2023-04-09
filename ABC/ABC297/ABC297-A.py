"""
A, B = map(int, input().split())
#list型で取得
l = list(map(int, input().split()))
"""
N, D =  map(int, input().split())
T_list = list(map(int, input().split()))
pre_time = 0
for i in T_list:
    if i - pre_time <= D and pre_time != 0:
        print(i)
        exit()
    pre_time = i
print(-1)


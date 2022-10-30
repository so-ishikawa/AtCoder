N, M = map(int, input().split())

s_list = []
for i in range(M):
    s = list(map(int, input().split()))
    s.pop(0)
    s_list.append(s)

p_list = list(map(int, input().split()))

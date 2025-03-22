N = int(input())
A_list = list(map(int,input().split()))
A_list.insert(0, "dummy")

dic = dict()

for i in range(1, N+1):
    dic.setdefault(A_list[i], []).append(i)

_dic = {k: v for k, v in dic.items() if len(v) == 1}
if len(_dic) == 0:
    print(-1)
    exit()

print(_dic[max(_dic)][0])

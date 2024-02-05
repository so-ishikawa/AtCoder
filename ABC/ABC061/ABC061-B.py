N, M = map(int, input().split())
dic = dict()
for i in range(1, N+1):
    dic[i] = list()

for i in range(M):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

for i in range(1, N+1):
    print(len(dic[i]))

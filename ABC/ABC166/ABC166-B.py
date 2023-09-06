N, K = map(int, input().split())
dic = dict()
for i in range(1, N+1):
    dic[i] = 0

for i in range(K):
    d = int(input())
    a_list = list(map(int, input().split()))
    for j in a_list:
        dic[j] = dic[j] + 1

print(sum([v == 0 for v in dic.values()]))


# from collections import defaultdict

# dic = defaultdict(lambda: 0)
N, Q = map(int, input().split())
dic = dict()
for i in range(1, N+1):
    dic[i] = 0

T_list = list(map(int, input().split()))

for t in T_list:
    dic[t] = dic[t] + 1

print(len([x for x in dic.values() if x % 2 == 0]))

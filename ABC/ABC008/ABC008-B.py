from collections import defaultdict
dic = defaultdict(lambda: 0)

N = int(input())
for _ in range(N):
    temp = input()
    dic[temp] = dic[temp] + 1

print(max(dic, key=dic.get))

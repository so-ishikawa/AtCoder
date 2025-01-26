N = int(input())
dic = {}

for i in range(N):
    S = input()
    dic[S] = dic.get(S, 0) + 1

max_count = max(dic.values())

temp = [key for key, value in dic.items() if value == max_count]


temp.sort()
for i in temp:
    print(i)

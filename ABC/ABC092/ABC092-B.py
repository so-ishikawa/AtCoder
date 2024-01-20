from collections import defaultdict

N = int(input())
D, X = map(int, input().split())
A_list = []
for _ in range(N):
    A_list.append(int(input()))

dic = defaultdict(lambda: 0)

for a in A_list:
    temp = 0
    while True:
        if temp * a + 1 > D:
            break
        dic[temp * a + 1] = dic[temp*a+1]+1
        temp += 1
# print(dic)
print(sum(dic.values())+X)

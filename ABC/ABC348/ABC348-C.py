N = int(input())

dic = dict()
for i in range(N):
    A, C = map(int, input().split())
    if C in dic:
        dic[C].append(A)
        continue
    dic[C] = [A]

max_value = 0
for k in dic.keys():
    temp = min(dic[k])
    if max_value < temp:
        max_value = temp

print(max_value)

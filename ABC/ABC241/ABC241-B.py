N, M = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

dic = dict()
for a in A_list:
    if a not in dic:
        dic[a] = 1
        continue
    else:
        dic[a] = dic[a] + 1
        continue

for b in B_list:
    if b not in dic:
        print("No")
        exit()
    if dic[b] == 0:
        print("No")
        exit()
    dic[b] = dic[b] - 1

print("Yes")
exit()

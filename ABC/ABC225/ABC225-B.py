N = int(input())
dic = dict()

for i in range(N-1):
    a, b = map(int, input().split())
    if a in dic:
        dic[a].add(b)
    else:
        dic[a] = set({b})
    if b in dic:
        dic[b].add(a)
    else:
        dic[b] = set({a})

if max([len(x) for x in dic.values()]) == N-1:
    print("Yes")
    exit()

print("No")
exit()

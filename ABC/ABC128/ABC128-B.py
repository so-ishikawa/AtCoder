N = int(input())
temp = []
for i in range(N):
    s, p = map(str, input().split())
    temp.append((s,int(p),i+1))

temp.sort(key=lambda x: (x[0], -x[1]))
for i in temp:
    print(i[2])


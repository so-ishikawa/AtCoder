N = int(input())
ST_list = []

for i in range(N):
    s, t = map(str, input().split())
    ST_list.append((s, int(t)))

ST_list.sort(key=lambda x: x[1], reverse=True)
# print(ST_list)
print(ST_list[1][0])

N, M = map(int, input().split())
dic = dict()

fix_position = dict()
for i in range(1, N+1):
    fix_position[i] = None
fix_position[1] = (0, 0)
# print(fix_position)
for i in range(M):
    a, b, x, y = map(int, input().split())
    dic[(a, b)] = (x, y)
    dic[(b, a)] = (-x, -y)


for i in range(1, N):
    for j in range(i, N+1):
        if fix_position[i] == None:
            continue
        if fix_position[j] != None:
            continue
        if (i, j) not in dic:
            continue
        position = dic[(i, j)]
        fix_position[j] = (fix_position[i][0] + position[0], fix_position[i][1] + position[1])

for i in range(1, N+1):
    ans = fix_position[i]
    if ans == None:
        print("undecidable")
        continue
    print(ans[0], ans[1])


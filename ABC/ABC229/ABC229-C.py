N, W = map(int, input().split())
AB_list = []
for i in range(N):
    A, B = map(int, input().split())
    AB_list.append((A, B))

AB_list.sort(reverse=True)

temp = 0
for i in AB_list:
    A = i[0]
    B = i[1]
    if W > B:
        W = W - B
        temp += A*B
        continue
    if W == B:
        temp += A*B
        break
    if W < B:
        temp += A*W
        break
print(temp)

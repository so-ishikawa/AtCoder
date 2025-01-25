N, K = map(int, input().split())
temp = []
for i in range(N):
    p1, p2, p3 = map(int, input().split())
    temp.append((i, p1+p2+p3))

temp.sort(key=lambda x: -x[1])

target_score = temp[K-1][1]

temp.sort(key=lambda x: x[0])

for i in temp:
    # print(i[1])
    if i[1] + 300 >= target_score:
        print("Yes")
        continue
    print("No")
#print(temp, target_score)

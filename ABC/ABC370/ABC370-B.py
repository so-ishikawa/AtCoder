N = int(input())
hyo = []
hyo.append(None)

for i in range(1, N+1):
    temp = list(map(int, input().split()))
    temp.insert(0, None)
    hyo.append(temp)

elm = 1
for j in range(1, N+1):
    if elm >= j:
        elm = hyo[elm][j]
    else:
        elm = hyo[j][elm]
print(elm)

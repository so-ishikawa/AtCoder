src = []
for i in range(4):
    src.append(input().replace(" ",""))

for i in range(3, -1, -1):
    for j in range(3, -1, -1):
        print(src[i][j], end=" ")
    print("")

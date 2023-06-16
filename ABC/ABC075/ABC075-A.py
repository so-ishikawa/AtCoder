A, B, C = map(int, input().split())
temp = [A, B, C]
for i in temp:
    if temp.count(i) == 1:
        print(i)
        exit()


N = int(input())

for i in range(1, 9+1):
    temp = int(str(i)*3)
    if temp - N < 0:
        continue
    print(temp)
    exit()

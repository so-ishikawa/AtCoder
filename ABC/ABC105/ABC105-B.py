N = int(input())

for i in range(0, 100+4, 4):
    temp = N - i
    if temp == 0:
        print("Yes")
        exit()
    if temp < 0:
        print("No")
        exit()
    if temp % 7 == 0:
        print("Yes")
        exit()

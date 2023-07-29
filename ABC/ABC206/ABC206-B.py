N = int(input())

temp = 0
count = 1
while True:
    temp += count
    if temp >= N:
        print(count)
        exit()
    count += 1

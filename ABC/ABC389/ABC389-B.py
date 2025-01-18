X = int(input())
count = 1
temp = 1
while True:
    temp = temp * count
    
    if temp == X:
        print(count)
        exit()
    count += 1

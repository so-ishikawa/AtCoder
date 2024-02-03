N = int(input())

temp = list(range(1, N+1))
count = 0
while True:
    if len(temp) == 1:
        break
    temp = [x for x in temp if x % (2**count) == 0]
    count += 1
print(temp[0])
